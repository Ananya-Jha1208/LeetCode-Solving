class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            ans = [root.val]
            for node in root.children:
                ans += self.preorder(node)
            return ans
