# Find First and Last Position of Element in Sorted Array (LC 34)
# Verified 2026-07-31 — O(log n) time, O(1) space — LeetCode Accepted
#
# The problem looks like it needs two different searches. It needs one
# search called twice.
#
# Plain binary search is USELESS here: on [5,7,7,8,8,10] target 8 it
# lands on index 4, and which 8 it lands on is an accident of where mid
# fell. Change the array length and the answer moves. There is nothing
# to build on.
#
# The fix is to stop treating equality as "done". On a hit, keep going
# left. That turns the search into a LOWER BOUND — "first index where
# nums[i] >= target" — which is a stable, well-defined answer.
#
#   [0, l)   confirmed <  target
#   [h, n)   confirmed >= target   <- h is a LIVE candidate, not discarded
#   [l, h)   still unknown
#
# The thing that looks wrong and isn't: `h = mid` on a hit puts a
# confirmed match into the "ruled out" region. The answer isn't lost
# because l climbs until it meets h. h means "best candidate so far",
# not "rejected".
#
# Getting the LAST occurrence without writing a second, mirrored search:
#
#   nums:   5    7    7    8    8   10    (end)
#   index:  0    1    2    3    4    5      6
#                          ^^^^^^^^
#   lowerBound(8) -> 3     where the 8s BEGIN         -> first
#   lowerBound(9) -> 5     where things bigger START  -> last = 5 - 1
#
# On integers ">= 9" and "> 8" are the same statement, so target+1 asks
# "where do the bigger values start?" using the identical function.
# Never search for the last 8; search for the first non-8 and step back.
#
# THE GUARD. lowerBound always returns a SLOT, never a "not found":
#     lowerBound(6)  -> 1   but nums[1] is 7, target absent
#     lowerBound(99) -> 6 == len(nums), no such index, reading it crashes
# So the caller must ask the question the helper refuses to answer.
# Order matters — `or` short-circuits, so the bounds check must come
# first or case 2 crashes before the guard runs.
#
# Two O(log n) calls is still O(log n). Constant multipliers don't
# survive Big-O.
#
# Python ships this as bisect.bisect_left / bisect_right. Fine in a
# timed OA; useless as training, because the OA question that is SHAPED
# like a lower bound but isn't literally bisect_left — First Bad
# Version, Minimum in Rotated Sorted Array, Capacity To Ship Packages —
# needs the hand-built version to stand on.


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo = self.lowerBound(nums, target)
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        hi = self.lowerBound(nums, target + 1)
        return [lo, hi - 1]

    def lowerBound(self, nums: list[int], target: int) -> int:
        l = 0
        h = len(nums)              # exclusive bound
        while l < h:               # ...so l == h means the window is empty
            mid = (l + h) // 2
            if nums[mid] >= target:
                h = mid            # candidate — keep it, search left
            else:
                l = mid + 1        # mid is too small, discard it
        return l                   # where the two met = the answer


if __name__ == "__main__":
    sol = Solution()

    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 7) == [1, 2]

    # target absent but in range — lowerBound returns a valid-looking slot
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

    # target past the end — lowerBound returns len(nums); the bounds
    # check must fire BEFORE nums[lo] or this raises IndexError
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 99) == [-1, -1]
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 1) == [-1, -1]

    assert sol.searchRange([], 0) == [-1, -1]
    assert sol.searchRange([1], 1) == [0, 0]
    assert sol.searchRange([1], 2) == [-1, -1]

    # every element identical — first and last span the whole array
    assert sol.searchRange([2, 2, 2, 2], 2) == [0, 3]

    # target at each end
    assert sol.searchRange([1, 2, 3], 1) == [0, 0]
    assert sol.searchRange([1, 2, 3], 3) == [2, 2]

    print("all tests pass")
