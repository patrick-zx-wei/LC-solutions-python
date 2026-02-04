# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root: TreeNode) -> List[int]:
            if root is None:
                return []
            left = traverse(root.left)
            right = traverse(root.right)

            curr = [root.val]
            curr.extend(right)
            if len(left) > len(right):
                curr.extend(left[len(right):])
            return curr 
                

        return traverse(root)
