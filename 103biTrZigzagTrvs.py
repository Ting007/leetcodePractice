class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree = []
        tree_val= []
        if root:
            tree.append([root])
            tree_val.append([root.val])
        flag = 0
        for nodes in tree:
            sub = []
            sub_val = []
            for i in range(len(nodes)-1, -1, -1):
                if flag%2 == 1:
                    self.leftToright(nodes[i], sub, sub_val)
                if flag%2 == 0:
                    self.rightToleft(nodes[i], sub, sub_val)
            flag += 1
            if sub != []:
                tree.append(sub)
                tree_val.append(sub_val)
                
        return tree_val
    
    def rightToleft(self, node, sub, sub_val):
        if node.right:
            self.addright(node, sub, sub_val)
        if node.left:
            self.addLeft(node, sub, sub_val)
    
    def leftToright(self, node, sub, sub_val):
        if node.left:
            self.addLeft(node, sub, sub_val)
        if node.right:
            self.addright(node, sub, sub_val)
        
        
    def addLeft(self, node, sub, sub_val):
        sub.append(node.left)
        sub_val.append(node.left.val)
    
    def addright(self, node, sub, sub_val):
        sub.append(node.right)
        sub_val.append(node.right.val)