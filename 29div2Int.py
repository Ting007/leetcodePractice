class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a, b, res= abs(dividend), abs(divisor), 0
        while a >= b:
            x = 0
            while a >= b << (x+1):
                x += 1
            res += 1 << x
            a -= b << x
        return min(res if (divisor*dividend) > 0 else -res, 2147483647)

if __name__ == '__main__':
    foo = Solution()
    x = foo.divide(10, 3)
    print(x)