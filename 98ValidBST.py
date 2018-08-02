class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = []
        self.inOrderTravel(root, nodes)
        for a, b in zip(nodes, nodes[1:]):
            if a >= b:
                return False
        return True
        
    def inOrderTravel(self, root, nodes):
        if root and root.left:
            self.inOrderTravel(root.left, nodes)
        if root:
            nodes.append(root.val)
        if root and root.right:
            self.inOrderTravel(root.right, nodes)