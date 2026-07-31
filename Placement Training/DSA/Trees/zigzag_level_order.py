# Binary Tree Zigzag Level Order Traversal (LC 103)
# Verified 2026-07-31 — O(n) time, O(n) space — LeetCode Accepted
#
# Third variation on the same BFS skeleton (see level_order_traversal.py
# and level_order_bottom_up.py). Build each level left-to-right as usual,
# then reverse it on alternate levels.
#
# The only new state is a level counter. Root level (count 1) stays
# left-to-right; every even count gets flipped.
#
# Bug hit while writing this: `flag += 1` was placed INSIDE the
# `for _ in range(size)` loop, so it counted nodes instead of levels.
# Level [9, 20] bumped it twice, so the parity check saw the wrong value
# from level 1 onward.
#
# This is the exact inverse of the LC 107 bug, where the per-node child
# pushes drifted out to level scope. Same question both times: does this
# line fire once per node, or once per level? Anything reading node.* is
# per-node (inside the for). Anything about the level as a whole — the
# counter, the level list, res.append — is per-level (outside the for).


from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root) -> list[list[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])
        flag = 0
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
            flag += 1                  # per LEVEL, not per node
            if flag % 2 == 0:
                res.append(level[::-1])
            else:
                res.append(level)
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.zigzagLevelOrder(None) == []
    assert sol.zigzagLevelOrder(TreeNode(1)) == [[1]]

    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.zigzagLevelOrder(t) == [[3], [20, 9], [15, 7]]

    # four levels — checks the alternation actually alternates, not just flips once
    #        1
    #       / \
    #      2   3
    #     /   / \
    #    4   5   6
    #   /
    #  7
    t2 = TreeNode(
        1,
        TreeNode(2, TreeNode(4, TreeNode(7))),
        TreeNode(3, TreeNode(5), TreeNode(6)),
    )
    assert sol.zigzagLevelOrder(t2) == [[1], [3, 2], [4, 5, 6], [7]]

    print("all tests pass")
