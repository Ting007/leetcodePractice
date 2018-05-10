class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        magicstr=[1]
        occur=[1]
        mstr=1
        total=1
        ones=1
        if n == 0:
        	return 0
        if n == 1:
        	return 1
        else:
	        while len(magicstr) < n:
	        	if total > len(magicstr):
	        		if magicstr[-1] ==1:
	        			magicstr.append(1)
	        			ones+=1
	        		else:
	        			magicstr.append(2)
	        	elif total == len(magicstr):
	        		if magicstr[-1] ==2:
	        			magicstr.append(1)
	        			ones+=1
	        		else:
	        			magicstr.append(2)
	        	else:
	        		occur.append(magicstr[mstr])
	        		total+= magicstr[mstr]
	        		mstr+=1
	        return ones
	        		




def main():
        foo = Solution()
        # S=[2,3,4]
        # C=[4,5,6]
        foo.magicalString(6)

if __name__ == "__main__":
        main()