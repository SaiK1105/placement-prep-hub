# Binary Tree Level Order Traversal II (LC 107) — bottom-up
# Verified 2026-07-31 — O(n) time, O(n) space — LeetCode Accepted 34/34
#
# Same BFS skeleton as level_order_traversal.py. The only real change:
# reverse the outer list at the end (`res[::-1]`) — inner, left-to-right
# order within each level is untouched.
#
# Bug hit while writing this: the guarded child-pushes
#     if node.left: q.append(node.left)
#     if node.right: q.append(node.right)
# were indented one level too shallow — under the `while`, not under the
# `for _ in range(size)`. That scopes the push to "once per level"
# instead of "once per node popped," so only the LAST node's children in
# each level get considered. On a right-heavy sample tree this is
# invisible (the last node IS the one with remaining children) — it only
# surfaces on a tree like [1,2,3,4,5], where node 1 (level 1) and node 2
# (level 2, not last) both have children that get silently dropped.
# Signature of this bug: sample passes, most hidden tests fail.


from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root) -> list[list[int]]:
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
            res.append(level)
        return res[::-1]


if __name__ == "__main__":
    sol = Solution()

    assert sol.levelOrderBottom(None) == []
    assert sol.levelOrderBottom(TreeNode(1)) == [[1]]

    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.levelOrderBottom(t) == [[15, 7], [9, 20], [3]]

    # the counterexample that surfaces the level-scope bug:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert sol.levelOrderBottom(t2) == [[4, 5], [2, 3], [1]]

    print("all tests pass")
