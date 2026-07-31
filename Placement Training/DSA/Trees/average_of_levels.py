# Average of Levels in Binary Tree (LC 637)
# Verified 2026-07-31 — O(n) time, O(n) space — LeetCode Accepted 66/66
#
# Fourth variation on the level-BFS skeleton, and the first one written
# clean on the first attempt — no scope bug, ~6 minutes.
#
# The skeleton never changes. Only the per-level reduction does:
#     LC 102  ->  res.append(level)
#     LC 107  ->  res.append(level), then reverse res at the end
#     LC 103  ->  res.append(level) or level[::-1] by parity
#     LC 637  ->  res.append(sum(level) / len(level))
#     LC 199  ->  res.append(level[-1])
#
# That is the transferable takeaway: "BFS by level" is one skeleton with
# a swappable reduction step, not five separate algorithms.
#
# len(level) is never zero — a level only exists because nodes were
# enqueued for it, so no div-by-zero guard is needed.


from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root) -> list[float]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum(level) / len(level))
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.averageOfLevels(None) == []
    assert sol.averageOfLevels(TreeNode(1)) == [1.0]

    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.averageOfLevels(t) == [3.0, 14.5, 11.0]

    # negatives — average can be fractional and negative
    t2 = TreeNode(-1, TreeNode(-2), TreeNode(5))
    assert sol.averageOfLevels(t2) == [-1.0, 1.5]

    print("all tests pass")
