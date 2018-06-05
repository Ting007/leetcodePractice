class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree = []
        tree_val= []
        if root:
            tree.append([root])
            tree_val.append([root.val])
        for nodes in tree:
            sub = []
            sub_val = []
            for node in nodes:
                if node.left:
                    sub.append(node.left)
                    sub_val.append(node.left.val)
                if node.right:
                    sub.append(node.right)
                    sub_val.append(node.right.val)
            if sub != []:
                tree.append(sub)
                tree_val.append(sub_val)
                
        return self.reverList(tree_val)
    
    def reverList(self, tree):
        rev_tree = []
        for i in range(len(tree)-1, -1, -1):
            rev_tree.append(tree[i])
        return rev_tree