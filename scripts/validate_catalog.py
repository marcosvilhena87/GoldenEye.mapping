"""Cross-reference validator for canonical GoldenEye mapping. Standard library only."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES = {"candidate", "observed", "reproduced", "validated", "rejected"}

def load(name):
    data = json.loads((ROOT / "catalog" / (name + ".json")).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{name}: expected an array")
    if any(not isinstance(item, dict) for item in data):
        raise ValueError(f"{name}: every item must be an object")
    ids = [item.get("id") for item in data]
    if any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
        raise ValueError(f"{name}: missing or duplicate id")
    return data

def validate():
    roms, evidence, symbols, behaviors = (load(n) for n in ("roms", "evidence", "symbols", "behaviors"))
    rom_ids = {r["id"] for r in roms}
    evidence_ids = {e["id"] for e in evidence}
    symbol_ids = {s["id"] for s in symbols}
    hashes = [r.get("sha256") for r in roms]
    if any(not isinstance(h, str) or len(h) != 64 or any(c not in "0123456789abcdefABCDEF" for c in h) for h in hashes):
        raise ValueError("roms: invalid SHA-256")
    if len(set(h.lower() for h in hashes)) != len(hashes):
        raise ValueError("roms: duplicate hash")
    for group, rows in (("evidence", evidence), ("symbols", symbols), ("behaviors", behaviors)):
        for row in rows:
            if row.get("rom_id") not in rom_ids:
                raise ValueError(f"{group}/{row['id']}: unknown rom_id")
            if group != "evidence":
                if row.get("status") not in STATES:
                    raise ValueError(f"{group}/{row['id']}: invalid status")
                refs = row.get("evidence_ids")
                if not isinstance(refs, list) or any(ref not in evidence_ids for ref in refs):
                    raise ValueError(f"{group}/{row['id']}: invalid evidence links")
                if row["status"] in {"reproduced", "validated"} and not refs:
                    raise ValueError(f"{group}/{row['id']}: confirmed without evidence")
                if group == "behaviors":
                    if any(ref not in symbol_ids for ref in row.get("related_symbol_ids", [])):
                        raise ValueError(f"behaviors/{row['id']}: unknown symbol")
                else:
                    if row.get("width_bits") not in (8,16,32,64) or row.get("endianness") not in ("big","little","not_applicable"):
                        raise ValueError(f"symbols/{row['id']}: invalid width/endianness")
                    if row.get("domain") not in ("RDRAM","ROM","other"):
                        raise ValueError(f"symbols/{row['id']}: invalid domain")
                    resolution = row.get("resolution")
                    if not isinstance(resolution, dict) or resolution.get("kind") not in ("absolute", "pointer_chain", "unknown"):
                        raise ValueError(f"symbols/{row['id']}: invalid resolution")
                    if resolution["kind"] == "absolute" and (not isinstance(resolution.get("address"), str) or not resolution["address"].startswith("0x")):
                        raise ValueError(f"symbols/{row['id']}: address missing")
    print(f"VALID: {len(roms)} ROM(s), {len(evidence)} evidence item(s), {len(symbols)} symbol(s), {len(behaviors)} behavior(s)")

if __name__ == "__main__":
    validate()
