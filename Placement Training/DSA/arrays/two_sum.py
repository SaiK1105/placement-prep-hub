# Two Sum
# Given an array and a target, return indices of two numbers that add up to target.
# Constraints: exactly one solution exists, cannot use same element twice.

# Brute Force — O(n^2) time, O(1) space
def two_sum_brute(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]

# Optimized — O(n) time, O(n) space
def two_sum(arr, target):
    seen = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return [seen[complement], i]
        seen[arr[i]] = i
