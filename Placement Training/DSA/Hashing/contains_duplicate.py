# Contains Duplicate — Hell Week Day 1
# Verified 2026-07-23 — brute force O(n^2) correct but wasteful; optimized to O(n)
#
# Pattern signal: "have I seen this exact thing before, yes/no" -> hash SET
# (no extra data attached). Contrast Two Sum's hash MAP, where you needed a
# VALUE (the index) attached to each key (the number) -> dict, not set.
#
# Real bug hit while writing this: `set = set()` shadows the builtin `set`
# type with the variable name. Works once (RHS evaluates before the
# assignment binds), but is a landmine for any later `set()` call in the
# same scope. Fix: never name a variable after the type you're instantiating
# (use `s`, `seen`, etc.).


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    assert contains_duplicate([7]) is False
    print("all tests pass")
