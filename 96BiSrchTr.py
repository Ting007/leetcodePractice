class Solution(object):
    def __init__(self):
        self.result = {}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.result[0] = 1 
        self.result[1] = 1
        for i in range(2, n+1):
            j = 0
            sum = 0
            while j < i:
                sum+=self.result[i-j-1]*self.result[j]
                j += 1
            self.result[i] = sum
        return self.result[n]

def main():
        foo = Solution()
        print(foo.numTrees(4))

if __name__ == "__main__":
        main()