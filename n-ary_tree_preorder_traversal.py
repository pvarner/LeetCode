"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        newSiblings = root.children
        curSiblings = []
        l = []
        
        l.append(root.val)
        
        
        while len(newSiblings) > 0:
            l.append(None)
            curSiblings = newSiblings
            newSiblings = []
            
            for node in curSiblings:
                l.append(node.val)
                newSiblings.extend(node.children)
            
            
            
        
        