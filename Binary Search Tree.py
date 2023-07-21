class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val > val:
            return self.searchBST(root.left, val)
        elif root and root.val < val:
            return self.searchBST(root.right, val)
        return root
