class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
        	return 0
        S = "122"
        i = 2 # counter 
        j = 2 # identity
        
        while len(S) <= n:
        	insert = ''
        	if S[j] == '2':
        		S += '1'*int(S[i])
        	else:
        		S += '2'*int(S[i])
        	j += int(S[i])
        	i += 1
        return S[:n].count('1')

def main():
        foo = Solution()
        # S=[2,3,4]
        # C=[4,5,6]
        x = foo.magicalString(4)
        print(x)

if __name__ == "__main__":
        main()

