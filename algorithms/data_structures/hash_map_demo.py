"""Hash map demo: word counter."""

class HashMapDemo:
    @staticmethod
    def run():
        print("\n=== HASH MAP(word counter) ===")
        raw = input("Enter a sentence (default: the cat and the dog and the bird): ").strip()
        text = raw or "the cat and the dog and the bird"
        counts = {}
        for w in text.split():
            counts[w] = counts.get(w, 0) + 1
        for w, c in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {w:<10} {'█' * c} ({c})")