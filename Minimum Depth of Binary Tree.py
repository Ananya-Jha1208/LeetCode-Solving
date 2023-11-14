class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        lt = self.minDepth(root.left)
        rt = self.minDepth(root.right)

        if (lt != 0 and rt != 0):
            return min(lt, rt) + 1
        
        return lt + rt + 1
