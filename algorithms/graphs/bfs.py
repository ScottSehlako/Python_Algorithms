"""Breadth-first traversal."""

from collections import deque

class BFS:
    @staticmethod
    def traverse(graph, start):
        visited, order, q = {start}, [], deque([start])
        while q:
            u = q.popleft()
            order.append(u)
            for v in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order

    @staticmethod
    def run(graph=None, start="A"):
        print("\n=== BFS — Level Order Traversal ===")
        graph = graph or {
            "A": ["B", "C"], "B": ["D", "E"],
            "C": ["F"], "D": [], "E": ["F"], "F": []
        }
        order = BFS.traverse(graph, start)
        print(f"  Visited order: {' → '.join(order)}")
        print("  BFS finds shortest edges in unweighted graphs.")