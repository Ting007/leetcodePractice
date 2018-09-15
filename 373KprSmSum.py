class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        p1, p2, q1, q2 = 0, 0, 0, 1
        while p1 < len(nums1) and q1 < len(nums2):
            if q2 > len(nums1):
                result.append([nums1[p1], nums2[p2]])
            elif p1 > len(nums1):
                result.append([nums2[q1], nums1[q2]])
            elif nums1[p1] + nums2[p2] <= nums2[q1] + nums1[q2]:
                result.append([nums1[p1], nums2[p2]])
                p2 += 1
                if p2 == len(nums2):
                    p1 = p1+1
                    p2 = p1
            else:
                result.append([nums2[q1], nums1[q2]])
                q2 += 1
                if q2 == len(nums1):
                    q1 = q1+1
                    q2 = q1+1

        return result

if __name__ == '__main__':
    foo = Solution()
    x = foo.kSmallestPairs([1,7,11], [2,4,6], 4)
    print(x)
