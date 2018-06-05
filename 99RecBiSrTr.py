Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        queue = []
        self.traversal(root, queue)

        for i in range(len(queue)):
            if queue[i]:
                for j in range(i, len(queue)):
                    if queue[j] and queue[i].val > queue[j].val:
                        self.swap(queue[i], queue[j])
        
    def traversal(self, root, queue):
        if root.left:
            self.traversal(root.left, queue)
        queue.append(root)
        if root.right:
            self.traversal(root.right, queue)
        
    
    def swap(self, node1, node2):
        temp = node1.val
        node1.val = node2.val
        node2.val = temp