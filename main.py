
import argparse
import sys


def run_visual():
    try:
        import pygame
    except ImportError:
        print("pygame is not installed.")
        print("Run this command:  pip3 install pygame")
        sys.exit(1)

    from visualizer import main
    main()


def run_text(start, end):
    from graph import build_city
    from astar import astar

    positions, adjacency = build_city()
    all_places = list(positions.keys())

    if start not in all_places:
        print(f"ERROR: '{start}' not found. Available places:")
        for p in all_places:
            print(f"  - {p}")
        sys.exit(1)

    if end not in all_places:
        print(f"ERROR: '{end}' not found.")
        sys.exit(1)
    print("\n" + "=" * 55)
    print(f"  A* Pathfinder:  {start}  →  {end}")
    print("=" * 55)
    a_path, a_cost, a_visited, _ = astar(positions, adjacency, start, end)
    print(f"\nA* (A-Star):")
    print(f"  Path    : {' → '.join(a_path)}")
    print(f"  Cost    : {a_cost:.1f}")
    print(f"  Visited : {len(a_visited)} nodes explored")
    print()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="City Pathfinder — A*")
    parser.add_argument("--text",  action="store_true",
                        help="Run in terminal mode (no pygame)")
    parser.add_argument("--start", type=str, default="West Gate")
    parser.add_argument("--end",   type=str, default="Airport")
    args = parser.parse_args()
    if args.text:
        run_text(args.start, args.end)
    else:
        run_visual()
