class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = []
        zero = []
        for i in range(len(nums)):
        	if nums[i] == 0:
        		zero.append(i)

        if len(zero) >1:
        	for i in range(len(nums)):
        		products.append(0)
        elif len(zero) == 1:
        	product = 1
        	for i in range(len(nums)):
        		if i != zero[0]:
        			product = product *nums[i]
        	for i in range(len(nums)):
        		if i != zero[0]:
        			products.append(0)
        		else:
        			products.append(product)

        else:
        	product = 1
        	for i in range(len(nums)):
        		product = product *nums[i]
        	for i in range(len(nums)):
        		products.append(int(product/nums[i]))
        return products

def main():
	foo = Solution()
	s = [1,2,3,4]
	print(foo.productExceptSelf(s))
	s = [1, 0]
	print(foo.productExceptSelf(s))

if __name__ == '__main__':
	main()