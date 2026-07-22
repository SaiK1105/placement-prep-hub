# Top-K frequent search terms (Tredence OA style, LeetCode 692-shaped)
# Verified 2026-07-19 — n up to 1e5, tie-break: alphabetically smaller ranks first
#
# Pattern: count with Counter -> encode rank as (-count, term) so ascending
# tuple comparison gives highest-count-first, alphabetically-smallest-on-ties
# -> heapify ALL m distinct terms once -> heappop k times.
#
# Rejected approach: maintaining a fixed-size-k heap with eviction on push.
# Breaks on ties, because a plain (count, term) min-heap evicts the
# alphabetically SMALLER term first (wrong direction) and there's no clean
# way to "negate" a string the way you negate count. Heapify-everything-then-
# pop-k sidesteps the problem entirely.
#
# Complexity: O(n) count pass + O(m) heapify + O(k log m) pops = O(n + m + k log m)

import heapq
from collections import Counter


def top_k_terms(terms: list[str], k: int) -> list[str]:
    counts = Counter(terms)
    heap = [(-count, term) for term, count in counts.items()]
    heapq.heapify(heap)

    result = []
    i = 0
    while i < k:
        result.append(heapq.heappop(heap)[1])
        i += 1
    return result


if __name__ == "__main__":
    assert top_k_terms(["shoes", "tv", "shoes", "usb", "tv", "tv"], 2) == ["tv", "shoes"]
    assert top_k_terms(["pen", "shoes"], 2) == ["pen", "shoes"]  # tie -> alphabetical
    print("all tests pass")
