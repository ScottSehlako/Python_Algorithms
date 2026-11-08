"""Dijkstra's shortest path algorithm."""

import heapq


class Dijkstra:
    @staticmethod
    def shortest_path(graph, start):
        dist = {n: float("inf") for n in graph}
        prev = {n: None for n in graph}
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u].items():
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(heap, (nd, v))
        return dist, prev

    @staticmethod
    def reconstruct(prev, target):
        path = []
        while target is not None:
            path.append(target)
            target = prev[target]
        return path[::-1]

    @staticmethod
    def run(graph=None, start="A"):
        print("\n=== DIJKSTRA — Shortest Path ===")
        graph = graph or {
            "A": {"B": 4, "C": 2},
            "B": {"A": 4, "C": 5, "D": 10},
            "C": {"A": 2, "B": 5, "D": 3, "E": 7},
            "D": {"B": 10, "C": 3, "E": 1},
            "E": {"C": 7, "D": 1},
        }
        raw = input(f"Start node (default {start}, options {list(graph)}): ").strip()
        start = raw if raw in graph else start

        dist, prev = Dijkstra.shortest_path(graph, start)
        for node in sorted(dist):
            path = Dijkstra.reconstruct(prev, node)
            print(f"  → {node}: cost {dist[node]:>2}  path: {' → '.join(path)}")