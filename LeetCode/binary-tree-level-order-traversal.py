from typing import List, Optional


"""
--PROBLEM DETAILS--

102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Acceptance rate: %
Difficulty: Medium

--SUBMISSION DETAILS--

Status: Accepted
Langauge: Python
Runtime: 37ms (Beats 95%)
Memory: 17.05MB (Beats 16.16%)

Values correct as of: 21/11/2023

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Explore the tree in a breadth-first method storing only the previous nodes and the values of all of the nodes.

        Args:
            root (Optional[TreeNode]): The root of the tree

        Returns:
            List[List[int]]: The values of the nodes in level order traversal
        """
        # edge case
        if root is None:
            return []
        
        # to store the values of the nodes (the output of the program)
        output_tree = [[root.val]]
        
        # the nodes in the previous level 
        prev_level = [root]
        
        all_leaves = False
        
        # run until all the nodes in the current level are leaf nodes
        while all_leaves is False:
            all_leaves = True
            current_level = []
            current_output = []
            
            # for each node from left to right
            for node in prev_level:
                left = node.left
                right = node.right
                
                # ge the left child
                if left is not None:
                    current_level.append(left)
                    current_output.append(left.val)
                    
                # get the right child
                if right is not None:
                    current_level.append(right)
                    current_output.append(right.val)
                    
                # check if the current node has children
                if left is not None or right is not None:
                    all_leaves = False
            
            # update the previous level with current level
            prev_level = current_level
            output_tree.append(current_output)

        # because we have to check for children of nodes we will append an extra [] 
        # its quicker to just pop it at the end rather than checking this in the loop
        output_tree.pop()
        
        return output_tree