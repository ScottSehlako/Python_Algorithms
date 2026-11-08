"""A* (Dijkstra + heuristic)"""

import heapq

class AStar:
    @staticmethod
    def search(graph, start, goal, heuristic):
        open_set = [(0, start)]
        g = {start: 0}
        prev = {start: None}
        while open_set:
            _, u = heapq.heappop(open_set)
            if u == goal:
                path = []
                while u is not None:
                    path.append(u)
                    u = prev[u]
                return path[::-1]
            for v, w in graph[u].items():
                ng = g[u] + w
                if ng < g.get(v, float("inf")):
                    g[v] = ng
                    prev[v] = u
                    heapq.heappush(open_set, (ng + heuristic(v, goal), v))
        return None

    @staticmethod
    def run():
        print("\n=== A* — Heuristic Path Search ===")
        coords = {"A": (0, 0), "B": (1, 0), "C": (2, 0),
                  "D": (0, 1), "E": (1, 1), "F": (2, 1)}
        graph = {
            "A": {"B": 1, "D": 1},
            "B": {"A": 1, "C": 1, "E": 1},
            "C": {"B": 1, "F": 1},
            "D": {"A": 1, "E": 1},
            "E": {"B": 1, "D": 1, "F": 1},
            "F": {"C": 1, "E": 1},
        }

        def h(n, goal):
            x1, y1 = coords[n]
            x2, y2 = coords[goal]
            return abs(x1 - x2) + abs(y1 - y2)

        path = AStar.search(graph, "A", "F", h)
        print(f"  A* path: {' → '.join(path)}")
        print("  Used in GPS, games, robotics and guides search with a heuristic.")