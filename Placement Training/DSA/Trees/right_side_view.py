# Binary Tree Right Side View (LC 199) — Daily 3, problem 3
# Verified 2026-07-30 — O(n) time, O(n) space
#
# Cousin of level_order_traversal.py. Identical BFS skeleton; the ONLY
# change is what gets appended per level.
#
# The trap: "the visible node is node.right" is wrong. If a node has no
# right child, its LEFT child is the rightmost thing on the next level:
#
#      1
#     / \
#    2   3
#       /
#      4        -> [1, 3, 4].  4 is a LEFT child and still visible.
#
# Correct rule: the visible node is the LAST node of the level, whichever
# side it hangs from. BFS already produces the level in left-to-right
# order, so "last" is free.
#
# Optimization over the naive version: building a full `level` list just
# to read level[-1] wastes the rest. Track the last value instead — same
# O(n) time, drops the per-level allocation.


from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size - 1:      # last node of this level = the visible one
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


if __name__ == "__main__":
    assert right_side_view(None) == []
    assert right_side_view(TreeNode(1)) == [1]

    #    1
    #   / \
    #  2   3
    #   \   \
    #    5   4
    t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(t) == [1, 3, 4]

    # the counterexample that kills "always take node.right":
    #    1
    #   / \
    #  2   3
    #     /
    #    4
    t2 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    assert right_side_view(t2) == [1, 3, 4]

    # left-skewed — every node is visible, nothing blocks it
    skew = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert right_side_view(skew) == [1, 2, 3]

    print("all tests pass")
