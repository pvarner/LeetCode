# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curLevel = []
    nextLevel = []
    result = []

    def func(self):
        
        if self.curLevel:
            tmp=[]
            for node in self.curLevel:
                tmp.append(node.val)
            self.result.append(tmp)

            for node in self.curLevel:
                if node.left:
                    self.nextLevel.append(node.left)
                if node.right:
                    self.nextLevel.append(node.right)

            self.curLevel = self.nextLevel
            self.nextLevel = [] 
            self.func()



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root:
            self.curLevel.append(root)
            self.func()