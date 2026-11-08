"""Fibonacci — naive vs memoized."""

import time

class Fibonacci:
    @staticmethod
    def naive(n):
        return n if n < 2 else Fibonacci.naive(n - 1) + Fibonacci.naive(n - 2)

    @staticmethod
    def memo(n, _cache={}):
        if n < 2:
            return n
        if n in _cache:
            return _cache[n]
        _cache[n] = Fibonacci.memo(n - 1) + Fibonacci.memo(n - 2)
        return _cache[n]

    @staticmethod
    def run():
        print("\n=== FIBONACCI — recursion + memoization ===")
        raw = input("n (default 30): ").strip()
        n = int(raw) if raw.isdigit() else 30
        t0 = time.perf_counter(); a = Fibonacci.naive(n); t1 = time.perf_counter() - t0
        t0 = time.perf_counter(); b = Fibonacci.memo(n);  t2 = time.perf_counter() - t0
        print(f"  fib({n}) naive: {a}  ({t1:.4f}s)")
        print(f"  fib({n}) memo : {b}  ({t2:.6f}s)")
        print(f"   Speedup: ~{t1 / max(t2, 1e-9):,.0f}×")