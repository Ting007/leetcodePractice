class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ten = ['', 'X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        hun = ['', 'C','CC','CCC','CD','D','DC','DCC', 'DCCC','CM']
        tho = ['', 'M','MM','MMM']
        ones = num%10
        tens = num//10%10
        huns = num//100%10
        thos = num//1000%10
        return tho[thos]+hun[huns]+ten[tens]+one[ones]

def main():
	foo = Solution()
	s = [3, 4, 9, 58, 1994]
	for num in s:
		print(foo.intToRoman(num))

if __name__ == '__main__':
	main() 