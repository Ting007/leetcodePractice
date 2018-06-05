#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
        	return []
        
        return self.generateSubTree(1, n+1)

    def generateSubTree(self, start, end):
        if end == start:
        	return None

        tree = []
        for i in range(start, end):
        	left_sub = self.generateSubTree(start, i)
        	for left in left_sub or [None]:
        		right_sub = self.generateSubTree(i+1, end)
        		for right in right_sub or [None]:
        			root = TreeNode(i)
        			root.left = left
	        		root.right = right
	        		tree.append(root)
        return tree

def main():
	foo = Solution()
	print(foo.generateTrees(3))

if __name__ == '__main__':
	main()