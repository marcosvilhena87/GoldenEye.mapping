# Analog stick — BizHawk controller input (not ROM/RDRAM)

Canonical raw-input evidence: [catalog/controller_analog.json](../catalog/controller_analog.json).

## Captured in session `20261023T031912Z_297508`

BizHawk 2.11.1, NLua `joypad.getimmediate(1)`, `X Axis`, `Y Axis`:

| Movement phase | X | Y | Frame | Status |
|---|---:|---:|---:|---|
| neutral | 0 | 0 | 297508 | observed |
| up | 0 | 127 | 305476 | observed |
| down | 0 | -127 | 311250 | observed |
| left | -127 | 0 | 312151 | observed |
| right | 127 | 0 | 313182 | observed |
| up (operator shifted diagonal) | -90 | 89 | 305518 | observed, diagonal phase unconfirmed |
| up (operator shifted diagonal) | 90 | 90 | 305569 | observed, diagonal phase unconfirmed |

**Still pending:** explicit phase-tagged tests for up-left/up-right/down-left/down-right, deadzone, intermediate values, gameplay effects and independent repetitions. Do not label these `validated` across cores/controllers.

These numbers **are input values from the emulator**, not virtual/physical memory addresses, offsets, pointer chains or GoldenEye internal state. Do not populate `catalog/symbols.json` based on input-coordinate data. The ROM checksum for this capture was not provided; the ROM catalog entry does not prove the session's hash.

## Complete diagonal capture

In `GoldenEye.assistant`, run `analog_mapping_v1.lua` with repository root as current directory. In PowerShell, for each phase, execute the command **before** moving the stick, hold briefly, return to neutral, then proceed:

```powershell
python .\tools\send_analog_v1.py PHASE up_left
python .\tools\send_analog_v1.py PHASE up_right
python .\tools\send_analog_v1.py PHASE down_left
python .\tools\send_analog_v1.py PHASE down_right
python .\tools\send_analog_v1.py PHASE neutral_end
```

**These five commands are a checklist, not a single copy-paste batch**: physically perform and release each movement before sending the next phase. Export the complete `output/csv/analog_v1_samples.csv`, along with diagnostics, then record values with frame and phase; until then, negative-Y diagonals remain unknown.

## Diagonal phase capture completed (same session)

| Phase | Frame | X Axis | Y Axis | Status |
|---|---:|---:|---:|---|
| up_left | 324161 | -90 | 89 | observed in matching phase |
| up_right | 325145 | 90 | 90 | observed in matching phase |
| down_left | 326357 | -90 | -90 | observed in matching phase |
| down_right | 327606 | 89 | -90 | observed in matching phase |
| neutral_end | 328539 | 0 | 0 | observed phase snapshot |

All four diagonals were reported from `analog_v1_samples.csv` for session `20261023T031912Z_297508` via BizHawk `joypad.getimmediate`. These are **controller API output values**, not `RDRAM` addresses or memory symbols. Replication, deadzone, intermediate levels and in-game motion effects remain untested.
