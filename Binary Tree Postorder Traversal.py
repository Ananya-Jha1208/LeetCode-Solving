class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(curr_node):
            if curr_node.left:
                traverse(curr_node.left)
            if curr_node.right:
                traverse(curr_node.right)
            result.append(curr_node.val)
        if root:
            traverse(root)
        return result
