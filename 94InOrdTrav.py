# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
    	self.nodeList = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
        	return self.nodeList
        print(self.nodeList)
        self.nodeList = self.inorderTraversal(root.left)
        self.nodeList.append(root.val)
        self.nodeList = self.inorderTraversal(root.right)
        return self.nodeList


def main():
        foo = Solution()
        S = [5, 2, 3, 0, 7, 5]
        a = []
        for i in range(len(S)):
        	a.append(TreeNode(S[i]))
        	if i > 0:
	        	parent = math.ceil(i/2)-1
        		if i%2 == 1:
        			a[parent].left = a[i]
        		else:
        			a[parent].right = a[i]



        print(foo.inorderTraversal(a[0]))

if __name__ == "__main__":
        main()