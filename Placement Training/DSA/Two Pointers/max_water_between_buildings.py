# Maximum water between two buildings (Tredence OA style)
# Verified 2026-07-20 — solved as LeetCode 11 "Container With Most Water" variant
# https://leetcode.com/problems/container-with-most-water/ (Accepted, 65/65, 96th pct runtime)
#
# Formula difference from LC 11: this version uses width = j - i - 1
# (only the gap BETWEEN buildings), LC 11 uses width = j - i (buildings included).
#
# Invariant: always advance the pointer with the SMALLER height.
# Why safe: the taller side's pointer can never be the bottleneck — moving it
# keeps min() capped at the same value while width only shrinks, so that move
# can never beat what's already recorded. Only the smaller side has a chance
# to raise the min for future pairs.
#
# Pattern signal: pair of positions from opposite ends + a greedy elimination
# argument (the weaker endpoint can provably never be optimal) -> two pointers.
# NOT sliding window (no contiguous-run condition) or top-k/heap (no positional
# relationship between elements).


def max_water(heights: list[int]) -> int:
    i, j = 0, len(heights) - 1
    bmax = 0
    while i < j:
        if heights[i] < heights[j]:
            cmax = heights[i] * (j - i - 1)
            bmax = max(bmax, cmax)
            i += 1
        else:
            cmax = heights[j] * (j - i - 1)
            bmax = max(bmax, cmax)
            j -= 1
    return bmax


if __name__ == "__main__":
    assert max_water([2, 1, 3, 4, 6, 5]) == 8
    assert max_water([5]) == 0
    assert max_water([]) == 0
    print("all tests pass")
