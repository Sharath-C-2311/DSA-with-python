# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root):
        l=defaultdict(list)
        
        def inord(root,col,row):
            if root:
                inord(root.left,col-1,row+1)
                l[col].append((row,root.val))
                inord(root.right,col+1,row+1)
                
        inord(root,0,0)
        result = []
        print(l)
        for col in sorted(l.keys()):
            r = sorted(l[col],key=lambda x:(x[0],x[1]))
            result.append([val for row,val in r])
        return result
    
# 987. Vertical Order Traversal of a Binary Tree

# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), 
# its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. 
# The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. 
# There may be multiple nodes in the same row and same column. 
# In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.
