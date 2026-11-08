"""Depth-first traversal."""


class DFS:
    @staticmethod
    def traverse(graph, start):
        visited, order = set(), []

        def _go(u):
            if u in visited:
                return
            visited.add(u)
            order.append(u)
            for v in graph.get(u, []):
                _go(v)

        _go(start)
        return order

    @staticmethod
    def run(graph=None, start="A"):
        print("\n=== DFS — Depth First Traversal ===")
        graph = graph or {
            "A": ["B", "C"], "B": ["D", "E"],
            "C": ["F"], "D": [], "E": ["F"], "F": []
        }
        order = DFS.traverse(graph, start)
        print(f"  Visited order: {' → '.join(order)}")
        print("  DFS goes deep first and used for mazes, cycle detection.")