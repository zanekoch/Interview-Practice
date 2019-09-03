#!/usr/bin/env python3
# encoding: utf-8


'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


[10,5,15,null,null,6,20]

         10
        5   15
           6 20


'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    #idea is to use a recursive algorithm to look at all nodes
    #I think you can use either depth first or breadth first search bc you are guarenteed to hit all nodes either way
    #ok lets do depth first cause I feel like it, what do we need to check at each node?
    #check if its left left child is less than it and if so recursively call fxn on left, if false return false. same with right but >
    #will this guarentee it is also a BST? no can have a "zig zag" => keep upper and lower bounds
    #how to make sure it makes it all the way
    def isValidBST(self, root) -> bool:
        def recursor(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not recursor(node.left, lower, node.val):
                return False
            if not recursor(node.right, node.val, upper):
                return False
            return True
        return recursor(root, float("-inf"), float("inf"))
