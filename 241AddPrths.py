import re
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        #first find all the location of math operation
        operation = [pos for pos, char in enumerate(input) if char in ['+', '-', '*']]
        #case 1: there is no math operation
        compute = []
        if len(operation) == 0:
        	compute.append(int(input))
        	return compute
        if len(operation) ==1:
        	result = eval(input)
        	compute.append(result)
        	return compute

        for i in operation:
        	left = input[:i]
        	sign = input[i]
        	right = input[i+1:]
        	#print(left, sign, right)
        	r_result = self.diffWaysToCompute(right)
        	l_result = self.diffWaysToCompute(left)
        	for l in l_result:
        		for r in r_result:
        			final_input = str(l)+sign+str(r)
        			temp_cal=eval(final_input)
        			compute.append(temp_cal)
        return compute

    


def main():
	foo = Solution()
	s = "2*3-4*5"
	print(foo.diffWaysToCompute(s))
	s = "2-1-1"
	print(foo.diffWaysToCompute(s))

if __name__ == '__main__':
	main()