# Rotate Array — Hell Week Day 1 (final problem, all 5 morning DSA done)
# Verified 2026-07-24 — two versions: O(n) extra space, then O(1) in-place reversal trick
#
# Journey here: naive sequential in-place swaps (nums[i] <-> nums[(i+k)%n] for
# i in range(n)) are WRONG for rotation -- each swap corrupts a value a later
# iteration still needs to read, unlike e.g. reversing where paired swaps
# never overlap. Confirmed by testing, not just reasoning about it.
#
# Correct O(n)-space formula: res[i] = nums[(i-k) % n]  (PULL from i-k, not
# i+k -- (i+k)%n produces a LEFT rotation, the mirror-image bug).
#
# O(1) in-place trick (reversal method): rotating right by k is equivalent to
# swapping two blocks (last k elements, first n-k elements) with no extra
# space. Reverse the WHOLE array first -- this puts both blocks in the right
# POSITION but each block's internal order is now backwards. Reversing each
# block individually undoes just the internal reversal, leaving correct
# block placement. General signal: "relocate two blocks without extra
# space" -- same structural move used in string rotation and left-rotation
# (rotate first k, then remaining n-k, then swap reversal order).
#
# Edge case: k can exceed n. Always k %= n first, or slicing/indexing on the
# second block (nums[k-1], nums[k:]) goes out of bounds.


def rotate_extra_space(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    k %= n
    return [nums[(i - k) % n] for i in range(n)]


def rotate_in_place(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


if __name__ == "__main__":
    assert rotate_extra_space([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate_extra_space([1, 2], 3) == [2, 1]

    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_in_place(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums2 = [1, 2]
    rotate_in_place(nums2, 3)
    assert nums2 == [2, 1]

    print("all tests pass")
