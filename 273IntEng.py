class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',\
        'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty']
        res = ''

        if num < 100:
            if num < 20:
                res = ones[num]
            else:
                ten_digit = num//10
                if ten_digit > 0:
                    res = tens[ten_digit]
                if num%10 > 0:
                    res += self.numberToWords(num%10)

        elif num < 1000:
            hund_digit = num//100
            if hund_digit > 0:
                res = ones[hund_digit] + ' ' + 'Hundred '
            if num%100 > 0:
                res += self.numberToWords(num%100)


        elif num < 1000000:
            thou_digit = num //1000
            if thou_digit > 0:
                res = self.numberToWords(num//1000) + ' ' + 'Thousand '
            if num%1000 > 0:
                res += self.numberToWords(num%1000)

        elif num < 1000000000:
            million = num // 1000000
            if million > 0:
                res = self.numberToWords(num//1000000) + ' ' + 'Million '
            if num%1000000 > 0:
                res += self.numberToWords(num%1000000)

        else:
            billion = num // 1000000000
            if billion > 0:
                res = self.numberToWords(num//1000000000) + ' ' + 'Billion '
            if num%1000000000 > 0: 
                res += self.numberToWords(num%1000000000)
        return res

if __name__ == '__main__':
    foo = Solution()
    s = [0, 100, 2000, 10000000, 10000000000, 12421, 1000000000345678, 10, 20]
    for i in s:
        x = foo.numberToWords(i)
        print(x)