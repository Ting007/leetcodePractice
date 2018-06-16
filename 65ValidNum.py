class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        try:
            float(s)
        except:
            return False
        return True