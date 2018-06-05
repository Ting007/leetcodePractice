# Definition for a binary tree node.
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

        if n == 1:
            root = TreeNode(n)
            return [[root]]

        trees = self.generateSubTree(1, n+1) #example n = 3, nodes [1,2,3], start 1, end 4
        return trees


    def generateSubTree(self, start, end):
        
        if start >= end:# n = 0
            return None

        tree = []
        for i in range(start, end):# start=1, end = 4, i = 1,2,3
            for left in self.generateSubTree(start, i) or [None]:
                for right in self.generateSubTree(i+1, end) or [None]:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    tree.append(root)

        return tree
        

def main():
        foo = Solution()
        print("result is ")
        print(foo.generateTrees(3))

if __name__ == "__main__":
        main()

