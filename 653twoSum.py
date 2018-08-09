class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # nodes = set()
        # def dfs(root, k, nodes):
        # 	if root:
        # 		differ = k - i.val
        # 		if differ in nodes:
        # 			return True
        # 		nodes.add(i.val)
        # 	if root.left:
        # 		self.dfs(root.left, k, nodes)
        # 	if root.right:
        # 		self.dfs(root.right, k, nodes)
        # return False

        nodes = set()
        def dfs(root):
        	if not root:
        		return False
        	differ = k - root.val
        	if differ in nodes:
        		return True
        	nodes.add(root.val)
        	return dfs(root.left) or dfs(root.right)
        return dfs(root)




