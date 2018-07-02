class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B) or set(A) != set(B):
        	return False
        if A == B:
        	for letter in A:
        		if A.count(letter) >1:
        			return True
        index = []
        for i in range(len(A)):
        	if A[i] != B[i]:
        		index.append(i)
        if len(index) != 2:
        	return False
        return A[index[0]] == B[index[1]] and  A[index[1]] == B[index[0]] 

def main():
	A = "abab"
	B = "abab"
	foo = Solution()
	print(foo.buddyStrings(A, B))

if __name__ == '__main__':
	main()