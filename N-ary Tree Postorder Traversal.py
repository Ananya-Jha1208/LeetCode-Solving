class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            ans = []
            for node in root.children:
                ans += self.postorder(node)
            return ans + [root.val]
