# 🚌 BMTC Bus Route Finder — Route 285M

A Python CLI tool to find the bus number and all stops between any two stops on **BMTC Route 285M** (Kempegowda Bus Station ↔ Doddaballapura Old Bus Stand).

---

## Features

- **44 stops** — complete route 285M loaded
- **Both directions** — works Kempegowda → Doddaballapura and reverse
- **Any two stops** — enter start and end, get all stops between them in travel order
- **Case-insensitive** — `HEBBALA`, `hebbala`, `Hebbala` all work
- **Partial names** — `mekhri`, `jakkur`, `gkvk`, `crpf` all resolve correctly
- **Aliases** — `majestic` → Kempegowda BS, `wheel factory` → Rail Wheel Factory, etc.
- **No dependencies** — pure Python 3, nothing to install

---

## Usage

### Interactive mode (default)
```bash
python bus_finder.py
```
Then type your start and end stop when prompted.

### Command-line arguments
```bash
python bus_finder.py --from "Mekhri Circle" --to "Jakkur Aerodrum"
python bus_finder.py --from "doddaballapura" --to "majestic"
python bus_finder.py --from "crpf" --to "hebbala"
```

### List all 44 stops
```bash
python bus_finder.py --list
```

---

## Example Output

```
Enter START stop : Hebbala
Enter END stop   : Rajanukunte

────────────────────────────────────────────────────────
  Bus Number   :  285M
  Direction    :  Towards Doddaballapura
  From         :  Stop 10 — Hebbala (Towards Yalahanka)
  To           :  Stop 28 — Rajanukunte
  Total Stops  :  19
────────────────────────────────────────────────────────
  Stops on your journey (in travel order):

  ├─ 10. Hebbala (Towards Yalahanka)  ← START
  ├─ 11. Military Dairy Farm
  ├─ 12. Kodigehalli Gate
  ├─ 13. Byatarayanapura (Towards Yalahanka)
  ├─ 14. GKVK Gate (Towards Yalahanka)
  ├─ 15. Jakkur Aerodrum
  ├─ 16. Allalasandra Gate (Towards Yalahanka)
  ├─ 17. YHK Police Station
  ├─ 18. NES Office
  ├─ 19. Escorts
  ├─ 20. Rail Wheel Factory
  ├─ 21. Puttenahalli
  ├─ 22. Ananthapura Gate (Towards Doddaballapura)
  ├─ 23. CRPF (Towards Doddaballapura)
  ├─ 24. Nagenahalli Gate
  ├─ 25. Avalahalli (Towards Doddaballapura)
  ├─ 26. Singanayakanahalli Gate
  ├─ 27. Honnenahalli
  └─ 28. Rajanukunte  ← END
```

---

## Supported Aliases

| What you type | Resolves to |
|---|---|
| `majestic` | Kempegowda Bus Station |
| `kbs` | Kempegowda Bus Station |
| `hebbala` | Hebbala (Towards Yalahanka) |
| `gkvk` | GKVK Gate (Towards Yalahanka) |
| `jakkur` | Jakkur Aerodrum |
| `crpf` | CRPF (Towards Doddaballapura) |
| `yhk` | YHK Police Station |
| `wheel factory` | Rail Wheel Factory |
| `navodaya` | Navodaya School Doddaballapura |
| `doddaballapura` | Doddaballapura Old Bus Stand |
| `apparel park` | Aparel Park |

---

## Route — All 44 Stops

| # | Stop |
|---|---|
| 1 | Kempegowda Bus Station |
| 2 | KPCC Office |
| 3 | Shivananda Store |
| 4 | RM Guttahalli |
| 5 | Palace Ground |
| 6 | Mekhri Circle |
| 7 | CBI (Towards Hebbala) |
| 8 | Veterinary Hospital |
| 9 | Canara Bank Hebbala |
| 10 | Hebbala (Towards Yalahanka) |
| 11 | Military Dairy Farm |
| 12 | Kodigehalli Gate |
| 13 | Byatarayanapura (Towards Yalahanka) |
| 14 | GKVK Gate (Towards Yalahanka) |
| 15 | Jakkur Aerodrum |
| 16 | Allalasandra Gate (Towards Yalahanka) |
| 17 | YHK Police Station |
| 18 | NES Office |
| 19 | Escorts |
| 20 | Rail Wheel Factory |
| 21 | Puttenahalli |
| 22 | Ananthapura Gate (Towards Doddaballapura) |
| 23 | CRPF (Towards Doddaballapura) |
| 24 | Nagenahalli Gate |
| 25 | Avalahalli (Towards Doddaballapura) |
| 26 | Singanayakanahalli Gate |
| 27 | Honnenahalli |
| 28 | Rajanukunte |
| 29 | Sri Ramanahalli |
| 30 | Suradenapura Gate |
| 31 | Aradeshanahalli Gate (Towards Doddaballapura Road) |
| 32 | Marasandra Circle |
| 33 | Marasandra Govt School |
| 34 | Hosa Hudya |
| 35 | Jinke Bachahalli Gate |
| 36 | Railway Gate Bashettihalli |
| 37 | Bank Circle Bashettyhalli |
| 38 | Bashettihalli |
| 39 | Navodaya School Doddaballapura |
| 40 | Aparel Park |
| 41 | Railway Station Doddaballapura |
| 42 | Kasaba |
| 43 | Rangappa Circle |
| 44 | Doddaballapura Old Bus Stand |

---

## Requirements

- Python 3.6 or higher
- No external libraries needed

---

## License

MIT
