# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sumList = {}
        sumFreq=[]
        self.traversal(root, sumList)
        if len(sumList) > 0:
        	maxV = max(sumList.values())
        	for key, value in sumList.items():
        		if value >= maxV:
        			sumFreq.append(key)
        return sumFreq



    def traversal(self, root, sumList):#backorder traversal the tree
    	if root == None:
    		return 0
    	left = self.traversal(root.left, sumList)
    	right = self.traversal(root.right, sumList)
    	sum = left+right+ root.val
    	if sum not in sumList:
    		sumList[sum] = 1
    	else:
    		sumList[sum] += 1
    	return sum


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



        print(foo.findFrequentTreeSum(a[0]))

if __name__ == "__main__":
        main()

