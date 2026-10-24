"""Validate experimental candidates without promoting them to canonical symbols."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "catalog" / "candidates.json"
SYMBOLS = ROOT / "catalog" / "symbols.json"
ALLOWED = {"candidate", "observed", "reproduced", "rejected"}

def validate():
    rows = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    symbols = json.loads(SYMBOLS.read_text(encoding="utf-8"))
    if not isinstance(rows, list) or not isinstance(symbols, list):
        raise ValueError("Catalogs must contain arrays")
    ids = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Each candidate must be an object")
        cid = row.get("id")
        if not isinstance(cid, str) or not cid or cid in ids:
            raise ValueError("Missing or duplicated candidate ID")
        ids.add(cid)
        if row.get("status") not in ALLOWED:
            raise ValueError(f"{cid}: validated entries belong in catalog/symbols.json")
        if row.get("domain") not in ("RDRAM", "ROM", "other"):
            raise ValueError(f"{cid}: invalid domain")
        if not isinstance(row.get("offset_hex"), str) or not re.fullmatch(r"0x[0-9A-Fa-f]+",row["offset_hex"]):
            raise ValueError(f"{cid}: invalid offset")
        if row.get("width_bits") not in (8,16,32,64):
            raise ValueError(f"{cid}: invalid width")
        if row.get("operational_permission") != "read_only":
            raise ValueError(f"{cid}: candidates must remain read-only")
        if not isinstance(row.get("hypothesis"), str) or not row["hypothesis"]:
            raise ValueError(f"{cid}: hypothesis required")
        p = row.get("evidence_path")
        if not isinstance(p,str) or not p.startswith("experiments/") or not (ROOT/p).is_file():
            raise ValueError(f"{cid}: evidence file not found")
        if row.get("session_rom_verified") is not False or row.get("core_verified") is not False:
            raise ValueError(f"{cid}: this catalog records unverified-session candidates only; use reviewed symbols workflow for verified metadata")
    for row in symbols:
        if row.get("status") == "validated" and not row.get("evidence_ids"):
            raise ValueError("Validated symbols require evidence_ids")
    print(f"VALID: {len(rows)} experimental candidates; {len(symbols)} canonical symbols (unchanged)")

if __name__ == "__main__":
    validate()
