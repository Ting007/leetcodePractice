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
            return [[root.val]]

        trees = []
        #generate tree recursively by calling subtree
        nodeList = list(range(1, n+1))
        print(nodeList)
        self.generateSubTree(nodeList, n, trees)
        # while root.val != []:
        #     print(root, root.left, root.right)
        return trees


    def generateSubTree(self, nodeList, n, trees):
        if nodeList == []:
            return [None]
        # print("root is " + str(root.val))
        for i in range(1, n+1):
            root = TreeNode(nodeList[n-1])
            trees.append(root)


            leftList = list(range(1, i))
            if leftList != []:
                root.left=TreeNode(i-1)
            self.generateSubTree(leftList, i-1, trees)

            rightList = list(range(i, n))
            print("right is ")
            print(rightList)
            if rightList != []:
                root.right=TreeNode(rightList[-1])
            self.generateSubTree(rightList, root.val-1, trees)
        return trees
        

def main():
        foo = Solution()
        print("result is ")
        print(foo.generateTrees(3))

if __name__ == "__main__":
        main()

