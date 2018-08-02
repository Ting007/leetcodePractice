# class NumArray:

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.array = nums
        

#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: void
#         """
#         self.array[i] = val
        

#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return sum(self.array[i:(j+1)])

class NumArray:
    class BinaryIndexedTree:
        def __init__(self, n):
            self._sum = [0 for _ in range(n+1)]
        def update(self, i, delta):
            while i < len(self._sum):
                print(i)
                self._sum[i] += delta
                i += i & -i
        def query(self, i):
            s = 0
            while i > 0:
                s += self._sum[i]
                i -= i & -i
            return s

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums[:]
        self._tree = self.BinaryIndexedTree(len(nums))
        for i in range(len(nums)):
            self._tree.update(i+1, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self._tree.update(i+1, val - self._nums[i])
        self._nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._tree.query(j+1) - self._tree.query(i)

def main():
    obj = NumArray([1,2,3,4])
    obj.update(1, 0)
    x = obj.sumRange(1, 3)
    print(x)

if __name__ == '__main__':
    main()