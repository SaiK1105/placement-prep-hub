# Binary Tree Level Order Traversal — Daily 3, problem 2
# Verified 2026-07-30 — O(n) time, O(n) space
#
# Pattern signal: the problem wants nodes GROUPED BY DEPTH (or shortest
# distance from a source in an unweighted graph). Plain DFS visits every
# node too, but loses which level each node came from — that grouping is
# the only reason to pay for a queue.
#
# The whole trick is `size = len(q)` read ONCE before any popping. The
# queue grows while you pop (children get pushed), so `while len(q) > 0`
# as the inner condition swallows the entire tree and destroys the level
# boundary. Freezing the width first is what makes the boundary exist.
#
# Second trap: pushing node.left / node.right unguarded puts None in the
# queue, which crashes on the NEXT pop, not the current one.
#
# Space is O(n), not O(h): the widest level of a complete tree holds
# about n/2 nodes, and they are all in the queue at once.


from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        size = len(q)          # frozen BEFORE any pop — this is the level width
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)

    return res


if __name__ == "__main__":
    # empty tree
    assert level_order(None) == []

    # single node
    assert level_order(TreeNode(1)) == [[1]]

    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(t) == [[3], [9, 20], [15, 7]]

    # left-skewed — every level has exactly one node
    skew = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert level_order(skew) == [[1], [2], [3]]

    print("all tests pass")
