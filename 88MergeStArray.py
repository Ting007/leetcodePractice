class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        while n > 0 and m >0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if m == 0:
            nums1[:n] = nums2[:n]
        print(nums1)



def main():
    n1 = [2,4,6,8,0,0,0,0]
    n2 = [1,3,5,7]
    foo = Solution()
    x = foo.merge(n1, 4, n2, 4)

if __name__ == '__main__':
    main()