# shortest-path-finder
# 🗺️ City Pathfinder — A* Algorithm

A Python project that finds the **shortest path** between two places on a city map using the **A\* (A-Star)** algorithm with real-time visualization.

Made as a 1st year B.Tech AI/ML college project at VIT Bhopal.

---

## 🧠 How A* Works

A* finds the shorest path between two points on a graph (city map).

It uses this formla for every node:

```
f(n) = g(n) + h(n)
```

- `g(n)` = actual distance traveled from start to node n
- `h(n)` = estimated distance from n to goal (straight-line distance)
- `f(n)` = total estimated cost — A* always picks the node with lowest f(n) next

This makes A* **smarter** than regular algorithms — it aims toward the goal instead of searching everywhere.

---

## 📁 Files

```
shortest-path-finder/          ← root of your repo
│
├── main.py                    ← upload to root
├── requirements.txt           ← upload to root
├── README.md                  ← upload to root
├── .gitignore                 ← upload to root
│
└── pathfinder/                ← create this folder on GitHub
    ├── __init__.py
    ├── graph.py
    ├── astar.py
    └── visualizer.py
```

---

## ▶️ How to Run

```bash
# Install pygame
pip3 install pygame

# Run the project
python3 main.py

# Text mode (no pygame needed)
python3 main.py --text --start "West Gate" --end "Airport"
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| Click a node | Set as Start then End |
| S | Start / Pause |
| R | Reset |
| + / - | Speed |
| Q | Quit |

---

## 💡 Viva Questions

**Q: What is A\*?**
> A graph search algorithm that finds the shortest path using a heuristic to guide the search toward the goal.

**Q: What is g(n), h(n), f(n)?**
> g(n) = actual cost from start. h(n) = estimated cost to goal. f(n) = g(n) + h(n).

**Q: What heristic do we use?**
> Euclidean (straight-line) distance between two nodes.

**Q: Why is the heuristic admissible?**
> Straight-line distance never overestimates real distance, so A* always finds the shortest path.

**Q: What data structure does A\* use?**
> A min-heap (priority queue) — alwys picks the node with lowest f(n) next.

---

## 🛠️ Requirements

- Python 3.10+
- pygame
