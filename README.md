# 🐍 Python Algorithms Playground

An **interactive, animated, modular** showcase of classic algorithms and modern-market concepts — written in pure Python with **zero third-party dependencies**.

Every algorithm lives in its own file, its own class, and can be run standalone. The project ships with a terminal **menu**, **live animations**, and **head-to-head races** that benchmark algorithms on the *same* task.

> 💡 **No `pip install` needed.** Just Python 3.8+ and you're running in 5 seconds.

---

## 🚀 Quick Start

```bash
git clone https://github.com/<you>/<repo>.git
cd <repo>
python main.py
```

You'll see:

```
🐍 PYTHON ALGORITHMS — MAIN MENU
============================================================
   1. Stack (interactive)
   2. Queue (interactive)
   3. Linked List (interactive)
   4. Hash Map (word counter)
   5. Hashing (SHA-256)
   6. Blockchain (proof of work)
   7. Fibonacci (recursion vs memo)
   8. Regex (emails/dates/redaction)
   9. Dijkstra (shortest path)
  10. BFS (breadth-first)
  11. DFS (depth-first)
  12. A* (heuristic search)
  13. 🎬 Animate: Bubble Sort
  14. 🎬 Animate: Binary Search
  15. 🏁 Race: Sorts
  16. 🏁 Race: Searches
   0. Quit
```

Pick a number, follow the prompts, watch it run.

---

## 📂 Project Layout

```
.
├── main.py                    ← entry point (menu)
├── requirements.txt           ← empty (stdlib only)
├── README.md
└── algorithms/
    ├── __init__.py
    ├── data_structures/       # Stack, Queue, LinkedList, HashMap
    ├── searching/             # Linear, Binary
    ├── sorting/               # Bubble, Insertion, Selection,
    │                          #   Merge, Quick, Heap, Counting
    ├── graphs/                # Dijkstra, BFS, DFS, A*
    ├── cryptography/          # SHA-256, Blockchain
    ├── regex_demos/           # Email / date / redaction patterns
    ├── recursion/             # Fibonacci (naive vs memoized)
    ├── animations/            # Live terminal bar-chart animations
    └── races/                 # Same-task benchmark races
```

Each folder has an `__init__.py` so you can import cleanly:

```python
from algorithms.sorting import QuickSort
print(QuickSort.sort([5, 2, 9, 1]))
```

---

## 🧠 Sorting Algorithms — Line-by-Line Explanation

Each `sort(arr)` **returns a new sorted list** and never mutates the input (except Bubble/Insertion/Selection, which copy internally first).

### 1. Bubble Sort — `O(n²)`

```python
def sort(arr):
    a = arr[:]                          # 1. copy input so we don't mutate caller
    n = len(a)                          # 2. store length
    for i in range(n):                  # 3. outer loop — one full pass per item
        swapped = False                 # 4. track if this pass did any swaps
        for j in range(n - i - 1):      # 5. inner loop shrinks each pass (last i items are sorted)
            if a[j] > a[j + 1]:         # 6. is this pair out of order?
                a[j], a[j + 1] = a[j + 1], a[j]   # 7. swap
                swapped = True          # 8. note that we swapped
        if not swapped:                 # 9. no swaps = already sorted → early exit
            break
    return a                            # 10. return sorted copy
```

**How it works:** bubbles the largest value to the end on each pass. Best case `O(n)` (already sorted), worst/average `O(n²)`. **Stable** ✅.

### 2. Insertion Sort — `O(n²)`

```python
def sort(arr):
    a = arr[:]                          # 1. copy
    for i in range(1, len(a)):          # 2. walk from second item forward
        key = a[i]                      # 3. grab current value
        j = i - 1                       # 4. look left
        while j >= 0 and a[j] > key:    # 5. slide larger values right
            a[j + 1] = a[j]             # 6. shift right
            j -= 1                      # 7. move j left
        a[j + 1] = key                  # 8. insert key into its slot
    return a                            # 9. return
```

**How it works:** builds a sorted prefix, inserting each new item where it belongs. **Very fast on nearly-sorted data** (`O(n)`). **Stable** ✅. Great default for small arrays (< ~32 items).

### 3. Selection Sort — `O(n²)`

```python
def sort(arr):
    a = arr[:]                          # 1. copy
    for i in range(len(a)):             # 2. walk each position
        m = i                           # 3. assume current is minimum
        for j in range(i + 1, len(a)):  # 4. scan remainder
            if a[j] < a[m]:             # 5. found a smaller one?
                m = j                   # 6. update min index
        a[i], a[m] = a[m], a[i]         # 7. swap min into place
    return a                            # 8. return
```

**How it works:** finds the minimum of the unsorted suffix and swaps it forward. **Always `O(n²)`** regardless of input. Only wins when **writes are expensive** (does at most `n-1` swaps). **Not stable** ❌.

### 4. Merge Sort — `O(n log n)`

```python
def _merge(l, r):                       # helper — merges two sorted lists
    out = []                            # 1. output buffer
    i = j = 0                           # 2. two cursors
    while i < len(l) and j < len(r):    # 3. walk both until one runs out
        if l[i] <= r[j]:                # 4. pick smaller (<= keeps it stable)
            out.append(l[i]); i += 1
        else:
            out.append(r[j]); j += 1
    out.extend(l[i:])                   # 5. append leftovers
    out.extend(r[j:])
    return out

def sort(arr):
    if len(arr) <= 1:                   # 1. base case
        return arr[:]
    mid = len(arr) // 2                 # 2. split in half
    return _merge(                      # 3. recurse, then merge
        MergeSort.sort(arr[:mid]),
        MergeSort.sort(arr[mid:])
    )
```

**How it works:** divide-and-conquer. Guaranteed `O(n log n)` regardless of input. **Stable** ✅. **Downside:** `O(n)` extra memory.

### 5. Quick Sort — `O(n log n)` average, `O(n²)` worst

```python
def sort(arr):
    if len(arr) <= 1:                   # 1. base case
        return arr[:]
    pivot = arr[len(arr) // 2]          # 2. pick middle as pivot
    left = [x for x in arr if x < pivot]    # 3. partition
    mid  = [x for x in arr if x == pivot]   # 4. equal items
    right= [x for x in arr if x > pivot]    # 5. greater items
    return QuickSort.sort(left) + mid + QuickSort.sort(right)  # 6. recurse
```

**How it works:** pick a pivot, split into `< pivot`, `= pivot`, `> pivot`, recurse on sides. **Very fast in practice** — often beats Merge. **Downside:** worst case `O(n²)` on adversarial input; this list-comprehension variant uses `O(n)` extra memory. **Not stable** ❌.

### 6. Heap Sort — `O(n log n)`

```python
def sort(arr):
    h = arr[:]                          # 1. copy
    heapq.heapify(h)                    # 2. build min-heap in O(n)
    return [heapq.heappop(h) for _ in range(len(h))]  # 3. pop n times
```

**How it works:** turn array into a **min-heap**, pop each element (always the smallest). `O(n log n)` guaranteed. **In-place in classic form** (this variant uses `O(n)` extra). **Not stable** ❌. Great when memory is tight in the C/in-place version.

### 7. Counting Sort — `O(n + k)` — 🚨 integer-only

```python
def sort(arr):
    if not arr:
        return []
    max_v = max(arr)                    # 1. find range
    counts = [0] * (max_v + 1)          # 2. bucket per value
    for v in arr:                       # 3. tally
        counts[v] += 1
    out = []                            # 4. expand buckets in order
    for i, c in enumerate(counts):
        out.extend([i] * c)
    return out
```

**How it works:** never compares — **counts occurrences** and rebuilds. **Fastest possible** when integers are bounded (`k ≈ n`). **Downside:** requires non-negative integers; blows up if `max(arr)` is huge. **Stable** ✅.

### 🔍 TL;DR Sorting Cheat Sheet

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Bubble    | n | n² | n² | O(1) | ✅ | Learning only |
| Insertion | n | n² | n² | O(1) | ✅ | Great for small/nearly-sorted |
| Selection | n² | n² | n² | O(1) | ❌ | Fewest swaps |
| Merge     | n log n | n log n | n log n | O(n) | ✅ | Predictable, external sort |
| Quick     | n log n | n log n | n² | O(log n)* | ❌ | Fastest in practice |
| Heap      | n log n | n log n | n log n | O(1)* | ❌ | Tight memory |
| Counting  | n+k | n+k | n+k | O(k) | ✅ | Integer-only, lightning fast |
| **Timsort** (built-in) | n | n log n | n log n | O(n) | ✅ | Hybrid — what `sorted()` uses |

\*This educational variant uses `O(n)` extra; classic in-place versions differ.

---

## 🌐 Graphs — Algorithms, Pros, Cons

Four graph algorithms ship in `algorithms/graphs/`. Each answers **"how do I move through connected things?"** — the answer depends on the graph.

### Dijkstra — `O((V + E) log V)`

```python
def shortest_path(graph, start):
    dist = {n: float("inf") for n in graph}     # 1. all distances = ∞
    prev = {n: None for n in graph}             # 2. path tracker
    dist[start] = 0                              # 3. start = 0
    heap = [(0, start)]                          # 4. priority queue
    while heap:
        d, u = heapq.heappop(heap)               # 5. closest unfinalized node
        if d > dist[u]:                          # 6. skip stale entries
            continue
        for v, w in graph[u].items():            # 7. relax edges
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, prev
```

**What it does:** finds the **shortest weighted path** from one start to every node.
**Pros:**
- ✅ Correct on **non-negative weights**
- ✅ Fast with a binary heap
- ✅ Foundation for routing (GPS, network packets)
**Cons:**
- ❌ **Fails on negative weights** (use Bellman-Ford)
- ❌ Explores blindly in all directions — no goal-direction
- ❌ Slower than A* when you know the target

### BFS — Breadth-First Search — `O(V + E)`

```python
def traverse(graph, start):
    visited, order, q = {start}, [], deque([start])   # 1. init
    while q:
        u = q.popleft()                               # 2. dequeue from FRONT
        order.append(u)                               # 3. record visit
        for v in graph.get(u, []):                    # 4. neighbors
            if v not in visited:
                visited.add(v); q.append(v)           # 5. mark + enqueue
    return order
```

**What it does:** visits nodes **level by level** outward from start.
**Pros:**
- ✅ Finds the **shortest path in unweighted graphs** (fewest edges)
- ✅ Simple, iterative, no recursion risk
- ✅ Great for "friends of friends", web crawling layers
**Cons:**
- ❌ Needs **`O(V)` memory** (queue holds a whole frontier)
- ❌ Doesn't handle weights (use Dijkstra)
- ❌ Can be enormous on wide graphs (social networks)

### DFS — Depth-First Search — `O(V + E)`

```python
def traverse(graph, start):
    visited, order = set(), []
    def _go(u):                                       # 1. recursive helper
        if u in visited: return                       # 2. base case
        visited.add(u); order.append(u)               # 3. visit
        for v in graph.get(u, []):
            _go(v)                                    # 4. recurse
    _go(start)
    return order
```

**What it does:** dives as deep as possible before backtracking.
**Pros:**
- ✅ **Low memory** (`O(depth)`) — great for deep graphs
- ✅ Natural for **cycle detection, topological sort, maze solving**
- ✅ Trivial to write recursively
**Cons:**
- ❌ **No shortest-path guarantee**
- ❌ **Recursion depth limit** (~1000 in Python) — can crash on big graphs
- ❌ Search order depends on neighbor order (non-deterministic feel)

### A* — A-Star — `O((V + E) log V)`

```python
def search(graph, start, goal, heuristic):            # heuristic(v, goal) → estimate
    open_set = [(0, start)]                            # 1. heap of (f, node)
    g = {start: 0}                                     # 2. real cost so far
    prev = {start: None}
    while open_set:
        _, u = heapq.heappop(open_set)                 # 3. lowest f-score
        if u == goal:                                  # 4. done — reconstruct
            path = []
            while u is not None:
                path.append(u); u = prev[u]
            return path[::-1]
        for v, w in graph[u].items():
            ng = g[u] + w                              # 5. real cost to neighbor
            if ng < g.get(v, float("inf")):
                g[v] = ng
                prev[v] = u
                heapq.heappush(open_set, (ng + heuristic(v, goal), v))  # 6. f = g + h
    return None
```

**What it does:** Dijkstra + a **heuristic guess** of distance to goal (`h`). Guide the search toward the target.
**Pros:**
- ✅ **Dramatically faster than Dijkstra** when a good heuristic exists
- ✅ **Optimal if the heuristic is admissible** (never overestimates)
- ✅ Backbone of **GPS routing, game NPC pathfinding, robotics**
**Cons:**
- ❌ **Requires a good heuristic** — bad ones kill performance
- ❌ **Not optimal if heuristic overestimates** (becomes greedy)
- ❌ More code than BFS/Dijkstra, easy to get wrong

### 🔍 TL;DR Graph Cheat Sheet

| Algorithm | Finds | Weighted? | Needs heuristic? | Best for |
|-----------|-------|-----------|------------------|----------|
| **BFS** | Shortest (edges) | ❌ | ❌ | Unweighted shortest path |
| **DFS** | Any path | ❌ | ❌ | Cycle detection, mazes, topo sort |
| **Dijkstra** | Shortest (weighted) | ✅ (≥0) | ❌ | Routing tables, network cost |
| **A\*** | Shortest (weighted) | ✅ (≥0) | ✅ | GPS, games, robotics |

---

## 📦 Class-by-Class Function Reference

Every class exposes **either `run()`** (interactive demo) **or well-named methods** (usable in code). Here's the full API.

### `data_structures/`

#### `StackDemo` — LIFO container
| Method | What it does | Complexity |
|--------|--------------|-----------|
| `__init__(items=None)` | Build stack from list | O(n) |
| `push(x)` | Add to top | O(1) |
| `pop()` | Remove & return top; raises if empty | O(1) |
| `peek()` | Look at top without removing | O(1) |
| `__len__()` | `len(stack)` | O(1) |
| `run()` | Interactive prompt | — |

#### `QueueDemo` — FIFO container
| Method | What it does | Complexity |
|--------|--------------|-----------|
| `__init__(items=None)` | Build from list | O(n) |
| `enqueue(x)` | Add to back | O(1) |
| `dequeue()` | Remove & return front | O(1) |
| `__len__()` | `len(queue)` | O(1) |
| `run()` | Interactive prompt | — |

#### `LinkedList` — singly linked
| Method | What it does | Complexity |
|--------|--------------|-----------|
| `__init__(items=None)` | Build from list | O(n²)* |
| `append(value)` | Add to tail | O(n) |
| `delete(value)` | Remove first match; returns bool | O(n) |
| `to_list()` | Convert to Python list | O(n) |
| `run()` | Interactive prompt | — |

\*Because each `append` walks to the tail. Fine for demos.

#### `HashMapDemo`
| Method | What it does |
|--------|--------------|
| `run()` | Prompt for a sentence, print word frequency bar chart |

---

### `searching/`

#### `LinearSearch`
| Method | What it does | Complexity |
|--------|--------------|-----------|
| `search(arr, target)` | Scan left→right; return index or `-1` | O(n) |

#### `BinarySearch`
| Method | What it does | Complexity |
|--------|--------------|-----------|
| `search(arr, target)` | Halve sorted array; return index or `-1` | O(log n) |

---

### `sorting/` — all share the same API

```python
SortedList = SomeSort.sort(arr)   # returns NEW list, does not mutate arr
```

| Class | `.sort(arr)` | Stable | Notes |
|-------|--------------|--------|-------|
| `BubbleSort` | ✅ | ✅ | Learning only |
| `InsertionSort` | ✅ | ✅ | Great small/nearly-sorted |
| `SelectionSort` | ✅ | ❌ | Minimal swaps |
| `MergeSort` | ✅ | ✅ | Predictable O(n log n) |
| `QuickSort` | ✅ | ❌ | Fastest in practice |
| `HeapSort` | ✅ | ❌ | Tight memory |
| `CountingSort` | ✅ | ✅ | Non-negative integers only |

---

### `graphs/`

#### `Dijkstra`
| Method | What it does |
|--------|--------------|
| `shortest_path(graph, start)` | → `(distances_dict, previous_dict)` |
| `reconstruct(previous, target)` | → path list from start to target |
| `run(graph=None, start="A")` | Interactive demo |

Graph format: `{"A": {"B": 4, "C": 2}, ...}` — weighted adjacency dict.

#### `BFS`
| Method | What it does |
|--------|--------------|
| `traverse(graph, start)` | → visit order list |
| `run(graph=None, start="A")` | Interactive demo |

Graph format: `{"A": ["B", "C"], ...}` — unweighted adjacency.

#### `DFS`
| Method | What it does |
|--------|--------------|
| `traverse(graph, start)` | → visit order list |
| `run(graph=None, start="A")` | Interactive demo |

Same format as BFS.

#### `AStar`
| Method | What it does |
|--------|--------------|
| `search(graph, start, goal, heuristic)` | → path list or `None` |
| `run()` | Demo on a 2×3 grid |

`heuristic(node, goal)` must return a number ≥ 0.

---

### `cryptography/`

#### `HashingDemo`
| Method | What it does |
|--------|--------------|
| `run()` | SHA-256 the user's input, show digest |

#### `Block` (helper class)
| Method | What it does |
|--------|--------------|
| `__init__(index, data, prev_hash, difficulty=3)` | Mine a new block |
| `_compute_hash()` | SHA-256 of the block fields |
| `_mine()` | Find nonce so hash starts with N zeros |

#### `BlockchainDemo`
| Method | What it does |
|--------|--------------|
| `run()` | Mine 2 blocks, show nonce + time |

---

### `regex_demos/`

#### `RegexDemo`
| Method | What it does |
|--------|--------------|
| `run()` | Extract emails, dates, redact digits |

---

### `recursion/`

#### `Fibonacci`
| Method | What it does | Complexity |
|--------|--------------|-----------|
| `naive(n)` | Pure recursion — teaches exponential cost | O(2ⁿ) |
| `memo(n)` | Same formula + cache | O(n) |
| `run()` | Times both side-by-side | — |

---

### `animations/`

#### `animate_bubble(values, delay=0.15)`
Clears screen, redraws bars, highlights the pair being compared each swap.

#### `animate_binary_search(sorted_arr, target, delay=0.5)`
Clears screen, redraws bars, highlights `low`/`mid`/`high`.

---

### `races/`

#### `race_sorts(values)`
Times **7 sort algorithms + Timsort** on the *same* array; prints a bar chart ranking fastest → slowest; asserts correctness on each.

#### `race_searches(values, target)`
Times **LinearSearch vs BinarySearch** on the *same* sorted array; prints speedup.

---

## 🧪 How to Use as a Library

Every class works standalone — no menu required:

```python
from algorithms.sorting import MergeSort, QuickSort
from algorithms.searching import BinarySearch
from algorithms.graphs import Dijkstra

arr = [5, 2, 9, 1, 7]
print(MergeSort.sort(arr))               # [1, 2, 5, 7, 9]
print(QuickSort.sort(arr))               # [1, 2, 5, 7, 9]
print(BinarySearch.search(sorted(arr), 7))   # 4

graph = {"A": {"B": 1, "C": 4}, "B": {"C": 2}, "C": {}}
dist, _ = Dijkstra.shortest_path(graph, "A")
print(dist)                              # {'A': 0, 'B': 1, 'C': 3}
```

Great for LeetCode practice, teaching, or embedding into other projects.

---

## 🎯 For Recruiters & Reviewers — What to Look At

If you're reviewing this repo, here's a 2-minute tour of what makes it interesting:

1. **Run `python main.py`** → pick **15 (Race: Sorts)** → see 7 algorithms benchmarked head-to-head on the same array, with correctness verified by `assert` and results in a bar chart.
2. **Pick 13 (Animate: Bubble Sort)** → watch the sort happen live, one comparison at a time.
3. **Pick 6 (Blockchain)** → mine a real SHA-256 proof-of-work block; see the nonce and mine time.
4. **Open `algorithms/sorting/`** → 7 files, ~30 lines each. Each is self-contained, documented with docstrings, and importable in isolation.
5. **Open `main.py`** → the menu wiring is 60 lines; adding an algorithm takes 3 lines.
6. **Check `requirements.txt`** → empty on purpose. **Zero dependencies** — no `pip install`, no virtualenv needed. Runs on any Python 3.8+.

### Design decisions worth noting

- **Modularity** — one class per file, one theme per folder, `__init__.py` for clean imports.
- **Interactive-first** — every demo accepts custom input, never hardcodes values.
- **Correctness-verified benchmarks** — `race_sorts` asserts each algorithm matches `sorted()` before timing.
- **Educational docstrings** — each file's top line states what it does and its complexity.
- **Real-world relevance** — SHA-256, blockchain, A*, and Dijkstra are all used in production systems today.
- **Zero friction** — no installs, no config, no environment setup. Clone → run.

---

## 🛠 Requirements

- **Python 3.8+**
- No third-party packages
- Works on Windows / macOS / Linux (terminal animations adapt via `cls`/`clear`)

---

## 🗺️ Roadmap (Ideas for PRs)

- [ ] Dynamic programming: Kadane, 0/1 Knapsack, LCS
- [ ] Trie for autocomplete
- [ ] Union-Find + Kruskal's MST
- [ ] Bellman-Ford (negative weights)
- [ ] Merkle tree (deeper blockchain dive)
- [ ] Sliding window / two-pointer patterns
- [ ] Unit tests (`pytest`) per algorithm
- [ ] GitHub Actions workflow — run `pytest` on push

---

## 📜 License

MIT — use it, fork it, teach with it.

---

## 🙌 Contributing

Found a bug? Want to add an algorithm? PRs welcome.

1. Fork → branch → commit
2. Follow the one-class-per-file pattern
3. Add the import to the relevant `__init__.py`
4. Wire it into `main.py` if it deserves a menu slot
5. Open a PR

---

*Built for learning, benchmarking, and showing off that algorithms are actually fun.* 🐍
