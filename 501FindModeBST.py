class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        nodes = {}
        self.inOrderTravel(root, nodes)
        mode = max(nodes.values())
        return list(k for k, v in nodes.items() if v == mode)


    def inOrderTravel(self, root, nodes):
        """
        :type root: TreeNode
        :type: nodes: dict
        :rtype: none
        """
        if root and root.left:
            self.inOrderTravel(root.left, nodes)
        if root:
            if root.val in nodes.keys():
                nodes[root.val] += 1
            else:
                nodes[root.val] = 1
        if root and root.right:
            self.inOrderTravel(root.right, nodes)