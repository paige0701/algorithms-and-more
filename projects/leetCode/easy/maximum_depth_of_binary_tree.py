class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1