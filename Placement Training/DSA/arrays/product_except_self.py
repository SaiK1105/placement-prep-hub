# Product of Array Except Self — Hell Week Day 1
# Verified 2026-07-24 — two versions: O(n) extra space, then O(1) extra space follow-up
#
# No division allowed. Zeros are the classic trap for anyone who tries
# "total product / nums[i]" anyway — this approach needs no special-casing.
#
# Recurring bug pattern (hit in BOTH loops of the O(1) version): once a
# running accumulator variable (p, then s) already holds the correct value
# on its own, don't ALSO multiply it against a neighboring array slot
# (res[i-1] or res[i+1]) "for good measure" — that double-counts. Root
# confusion: conflating "the running total" with "one more thing to combine
# it with". Antidote: before writing res[i] = X * Y, ask "does X alone
# already equal what I want?" If yes, Y doesn't belong there.
#
# O(1)-space specific trap: res[i] already holds prefix[i] (loop 1's work)
# BEFORE loop 2 touches it — loop 2 must multiply the running suffix INTO
# the existing res[i], never overwrite it via a neighboring res[i+1].


def product_except_self_extra_space(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    return [prefix[i] * suffix[i] for i in range(n)]


def product_except_self_o1_space(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    s = 1
    for i in range(n - 2, -1, -1):
        s *= nums[i + 1]
        res[i] *= s
    return res


if __name__ == "__main__":
    for fn in (product_except_self_extra_space, product_except_self_o1_space):
        assert fn([1, 2, 3, 4]) == [24, 12, 8, 6]
        assert fn([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
        assert fn([0, 0]) == [0, 0]
    print("all tests pass")
