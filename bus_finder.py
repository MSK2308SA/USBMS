"""
BMTC Bus Route Finder — Route 285M
====================================
Finds the bus number and all stops between any two stops on route 285M.
- Case-insensitive input
- Works with partial names and aliases
- Shows stops in the EXACT direction you travel (forward or reverse)

Usage:
    python bus_finder.py
    python bus_finder.py --from "Mekhri Circle" --to "Jakkur Aerodrum"
    python bus_finder.py --list
"""

import re
import argparse

# ─────────────────────────────────────────────
#  ROUTE 285M — All 44 stops in order
# ─────────────────────────────────────────────
STOPS = [
    "Kempegowda Bus Station",                               # 1
    "KPCC Office",                                          # 2
    "Shivananda Store",                                     # 3
    "RM Guttahalli",                                        # 4
    "Palace Ground",                                        # 5
    "Mekhri Circle",                                        # 6
    "CBI (Towards Hebbala)",                                # 7
    "Veterinary Hospital",                                  # 8
    "Canara Bank Hebbala",                                  # 9
    "Hebbala (Towards Yalahanka)",                          # 10
    "Military Dairy Farm",                                  # 11
    "Kodigehalli Gate",                                     # 12
    "Byatarayanapura (Towards Yalahanka)",                  # 13
    "GKVK Gate (Towards Yalahanka)",                        # 14
    "Jakkur Aerodrum",                                      # 15
    "Allalasandra Gate (Towards Yalahanka)",                # 16
    "YHK Police Station",                                   # 17
    "NES Office",                                           # 18
    "Escorts",                                              # 19
    "Rail Wheel Factory",                                   # 20
    "Puttenahalli",                                         # 21
    "Ananthapura Gate (Towards Doddaballapura)",            # 22
    "CRPF (Towards Doddaballapura)",                        # 23
    "Nagenahalli Gate",                                     # 24
    "Avalahalli (Towards Doddaballapura)",                  # 25
    "Singanayakanahalli Gate",                              # 26
    "Honnenahalli",                                         # 27
    "Rajanukunte",                                          # 28
    "Sri Ramanahalli",                                      # 29
    "Suradenapura Gate",                                    # 30
    "Aradeshanahalli Gate (Towards Doddaballapura Road)",   # 31
    "Marasandra Circle",                                    # 32
    "Marasandra Govt School",                               # 33
    "Hosa Hudya",                                           # 34
    "Jinke Bachahalli Gate",                                # 35
    "Railway Gate Bashettihalli",                           # 36
    "Bank Circle Bashettyhalli",                            # 37
    "Bashettihalli",                                        # 38
    "Navodaya School Doddaballapura",                       # 39
    "Aparel Park",                                          # 40
    "Railway Station Doddaballapura",                       # 41
    "Kasaba",                                               # 42
    "Rangappa Circle",                                      # 43
    "Doddaballapura Old Bus Stand",                         # 44
]

# ─────────────────────────────────────────────
#  ALIASES — alternate / shorthand names
#  Maps normalized string → 0-based stop index
# ─────────────────────────────────────────────
ALIASES = {
    # Stop 1 — Kempegowda Bus Station
    "kempegowda": 0, "kbs": 0, "majestic": 0,
    "kempegowda bus station": 0, "kempegowda bs": 0,
    # Stop 2
    "kpcc": 1, "kpcc office": 1,
    # Stop 3
    "shivananda": 2, "shivananda store": 2,
    # Stop 4
    "rm guttahalli": 3, "guttahalli": 3,
    # Stop 5
    "palace ground": 4,
    # Stop 6
    "mekhri": 5, "mekhri circle": 5,
    # Stop 7
    "cbi": 6, "cbi hebbala": 6,
    # Stop 8
    "veterinary": 7, "vet hospital": 7, "veterinary hospital": 7,
    # Stop 9
    "canara bank": 8, "canara bank hebbala": 8,
    # Stop 10
    "hebbala": 9, "hebbala yalahanka": 9,
    # Stop 11
    "military dairy": 10, "dairy farm": 10, "military dairy farm": 10,
    # Stop 12
    "kodigehalli": 11, "kodigehalli gate": 11,
    # Stop 13
    "byatarayanapura": 12, "byta": 12,
    # Stop 14
    "gkvk": 13, "gkvk gate": 13,
    # Stop 15
    "jakkur": 14, "jakkur aerodrum": 14, "jakkur airport": 14,
    # Stop 16
    "allalasandra": 15, "allalasandra gate": 15,
    # Stop 17
    "yhk": 16, "yhk police": 16, "yhk police station": 16, "nhk police": 16,
    # Stop 18
    "nes": 17, "nes office": 17,
    # Stop 19
    "escorts": 18,
    # Stop 20
    "rail wheel factory": 19, "wheel factory": 19,
    "rail wheel": 19, "oheel and excel plant": 19,
    # Stop 21
    "puttenahalli": 20,
    # Stop 22
    "ananthapura": 21, "ananthapura gate": 21,
    # Stop 23
    "crpf": 22, "crpf doddaballapura": 22,
    # Stop 24
    "nagenahalli": 23, "nagenahalli gate": 23,
    # Stop 25
    "avalahalli": 24,
    # Stop 26
    "singanayakanahalli": 25, "singanayakanahalli gate": 25,
    # Stop 27
    "honnenahalli": 26,
    # Stop 28
    "rajanukunte": 27,
    # Stop 29
    "sri ramanahalli": 28, "ramanahalli": 28,
    # Stop 30
    "suradenapura": 29, "suradenapura gate": 29,
    # Stop 31
    "aradeshanahalli": 30, "aradeshanahalli gate": 30,
    # Stop 32
    "marasandra": 31, "marasandra circle": 31,
    # Stop 33
    "marasandra school": 32, "marasandra govt school": 32,
    # Stop 34
    "hosa hudya": 33,
    # Stop 35
    "jinke bachahalli": 34, "jinke bachahalli gate": 34,
    # Stop 36
    "railway gate bashettihalli": 35, "bashettihalli gate": 35,
    # Stop 37
    "bank circle": 36, "bank circle bashettyhalli": 36,
    # Stop 38
    "bashettihalli": 37,
    # Stop 39
    "navodaya": 38, "navodaya school": 38, "navodaya school doddaballapura": 38,
    # Stop 40
    "aparel park": 39, "apparel park": 39, "aparrel park": 39,
    # Stop 41
    "railway station doddaballapura": 40, "doddaballapura railway station": 40,
    "doddaballapura station": 40,
    # Stop 42
    "kasaba": 41,
    # Stop 43
    "rangappa": 42, "rangappa circle": 42,
    # Stop 44
    "doddaballapura": 43, "doddaballapura old bus stand": 43,
    "doddaballapura bus stand": 43, "old bus stand doddaballapura": 43,
}


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def normalize(text: str) -> str:
    """Lowercase, strip special chars, collapse spaces."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def find_stop_index(user_input: str) -> int:
    """
    Find 0-based index of a stop from user input.
    Search order:
      1. Alias table (handles short names, common alternates)
      2. Exact normalized match
      3. Stop name starts with query
      4. Stop name contains query
      5. Query contains first significant word of stop name
    Returns -1 if not found.
    """
    q = normalize(user_input)
    if not q:
        return -1

    if q in ALIASES:
        return ALIASES[q]

    for i, stop in enumerate(STOPS):
        if normalize(stop) == q:
            return i

    for i, stop in enumerate(STOPS):
        if normalize(stop).startswith(q):
            return i

    for i, stop in enumerate(STOPS):
        if q in normalize(stop):
            return i

    for i, stop in enumerate(STOPS):
        first_word = normalize(stop).split()[0]
        if len(first_word) > 3 and first_word in q:
            return i

    return -1


# ─────────────────────────────────────────────
#  CORE LOGIC
# ─────────────────────────────────────────────

def find_bus(from_input: str, to_input: str) -> dict:
    """
    Find bus and all stops between two stops, preserving direction.

    Returns dict:
        found         : bool
        bus           : str  — always "285M" if found
        from_stop     : str  — matched start stop name
        to_stop       : str  — matched end stop name
        from_num      : int  — stop number (1-based)
        to_num        : int  — stop number (1-based)
        direction     : str  — "Towards Doddaballapura" or "Towards Kempegowda BS"
        segment       : list — all stops from→to in travel order
        total_stops   : int  — number of stops including start & end
        error         : str  — set only when found=False
    """
    from_idx = find_stop_index(from_input)
    to_idx   = find_stop_index(to_input)

    if from_idx == -1:
        return {"found": False, "error": f"Stop not found: '{from_input}'"}
    if to_idx == -1:
        return {"found": False, "error": f"Stop not found: '{to_input}'"}
    if from_idx == to_idx:
        return {"found": False, "error": "Start and end stops are the same."}

    # Build segment in the user's exact direction of travel
    going_forward = from_idx < to_idx
    if going_forward:
        segment = [(i, STOPS[i]) for i in range(from_idx, to_idx + 1)]
        direction = "Towards Doddaballapura"
    else:
        segment = [(i, STOPS[i]) for i in range(from_idx, to_idx - 1, -1)]
        direction = "Towards Kempegowda Bus Station"

    return {
        "found":       True,
        "bus":         "285M",
        "from_stop":   STOPS[from_idx],
        "to_stop":     STOPS[to_idx],
        "from_num":    from_idx + 1,
        "to_num":      to_idx + 1,
        "direction":   direction,
        "segment":     segment,          # list of (0-based index, stop name)
        "total_stops": len(segment),
    }


# ─────────────────────────────────────────────
#  DISPLAY
# ─────────────────────────────────────────────

LINE = "─" * 56

def print_result(result: dict) -> None:
    if not result["found"]:
        print(f"\n  ✗  {result['error']}\n")
        return

    print(f"\n{LINE}")
    print(f"  Bus Number   :  {result['bus']}")
    print(f"  Direction    :  {result['direction']}")
    print(f"  From         :  Stop {result['from_num']:>2} — {result['from_stop']}")
    print(f"  To           :  Stop {result['to_num']:>2} — {result['to_stop']}")
    print(f"  Total Stops  :  {result['total_stops']}")
    print(LINE)
    print("  Stops on your journey (in travel order):\n")
    for pos, (stop_idx, stop_name) in enumerate(result["segment"]):
        is_last = (pos == len(result["segment"]) - 1)
        connector = "  └─" if is_last else "  ├─"
        tag = ""
        if pos == 0:
            tag = "  ← START"
        elif is_last:
            tag = "  ← END"
        print(f"{connector} {stop_idx + 1:>2}. {stop_name}{tag}")
    print()


def print_all_stops() -> None:
    print(f"\n  Route 285M — All 44 Stops")
    print(f"  Kempegowda Bus Station → Doddaballapura Old Bus Stand\n")
    print(LINE)
    for i, stop in enumerate(STOPS):
        prefix = "  ┌" if i == 0 else ("  └" if i == len(STOPS) - 1 else "  ├")
        print(f"{prefix} {i + 1:>2}. {stop}")
    print()


# ─────────────────────────────────────────────
#  ENTRY POINTS
# ─────────────────────────────────────────────

def interactive_mode() -> None:
    print("\n" + "═" * 56)
    print("   BMTC Bus Route Finder — Route 285M")
    print("   Kempegowda Bus Station ↔ Doddaballapura")
    print("═" * 56)
    print("  Commands: 'stops' = list all  |  'quit' = exit\n")

    while True:
        from_input = input("  Enter START stop : ").strip()

        if from_input.lower() in ("quit", "exit", "q"):
            print("\n  Goodbye!\n")
            break

        if from_input.lower() == "stops":
            print_all_stops()
            continue

        if not from_input:
            print("  Please enter a stop name.\n")
            continue

        to_input = input("  Enter END stop   : ").strip()

        if to_input.lower() in ("quit", "exit", "q"):
            print("\n  Goodbye!\n")
            break

        if not to_input:
            print("  Please enter a stop name.\n")
            continue

        result = find_bus(from_input, to_input)
        print_result(result)

        again = input("  Search again? (y/n) : ").strip().lower()
        if again != "y":
            print("\n  Goodbye!\n")
            break
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="BMTC Bus Route Finder — Route 285M",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--from", dest="from_stop", help="Start stop name")
    parser.add_argument("--to",   dest="to_stop",   help="End stop name")
    parser.add_argument("--list", action="store_true", help="List all 44 stops")
    args = parser.parse_args()

    if args.list:
        print_all_stops()
        return

    if args.from_stop and args.to_stop:
        result = find_bus(args.from_stop, args.to_stop)
        print_result(result)
        return

    # No args — launch interactive mode
    interactive_mode()


if __name__ == "__main__":
    main()
