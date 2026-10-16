# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sametree(self,root,subroot):
        if root is None and subroot is None:
            return True
        if root and subroot and root.val==subroot.val:
            return self.sametree(root.left,subroot.left) and self.sametree(root.right,subroot.right) 
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if not subRoot:
            return True
        if self.sametree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot)) or (self.isSubtree(root.right,subRoot))