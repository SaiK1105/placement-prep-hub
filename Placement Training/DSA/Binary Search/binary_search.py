# Binary Search (LC 704)
# Verified 2026-07-31 — O(log n) time, O(1) space — LeetCode Accepted 47/47
#
# THE thing to remember about binary search is not the shape — it is that
# there are two self-consistent conventions for the high bound, and every
# classic bug comes from mixing cells across the two rows:
#
#   convention   init h      loop cond   move h
#   inclusive    len-1       l <= h      h = mid - 1
#   exclusive    len         l <  h      h = mid
#
# Bug hit while writing this: wrote `h = len(nums)-1` and `h = mid-1`
# (both INCLUSIVE) but `while l < h` (EXCLUSIVE). One row, all three
# cells — mixing them is the bug.
#
# Why it matters: with an inclusive h, index h is a real candidate, so
# the range [l, h] is still non-empty when l == h. `l < h` exits one
# iteration early and never checks that last element. Signature: fails
# on single-element arrays, and on any case where the target is the last
# surviving candidate.
#
#     nums = [5], target = 5  ->  l=0, h=0, `0 < 0` is False,
#                                 loop never runs, returns -1. Wrong.


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        h = len(nums) - 1          # inclusive bound
        while l <= h:              # ...so the range is non-empty at l == h
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1        # ...and mid is excluded, having been checked
        return -1


if __name__ == "__main__":
    sol = Solution()

    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # the case that exposes `l < h`:
    assert sol.search([5], 5) == 0
    assert sol.search([5], 3) == -1

    # target at either end — the other place an off-by-one shows up
    assert sol.search([1, 2, 3, 4, 5], 1) == 0
    assert sol.search([1, 2, 3, 4, 5], 5) == 4

    # two elements, both directions
    assert sol.search([1, 2], 2) == 1
    assert sol.search([1, 2], 0) == -1

    print("all tests pass")
