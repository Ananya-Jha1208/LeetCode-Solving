class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(curr_node):
            result.append(curr_node.val)
            if curr_node.left:
                traverse(curr_node.left)
            if curr_node.right:
                traverse(curr_node.right)
        if root:
            traverse(root)
        return result
