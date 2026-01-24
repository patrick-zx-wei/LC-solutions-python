class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            temp = p
            p = q
            q = temp

        while root is not None:
            if p.val > root.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
            else:
                return root
      `
