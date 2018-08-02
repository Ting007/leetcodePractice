class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums
        self.tree = [ 0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            val = nums[i]
            i += 1
            while i < len(self.tree):
                self.tree[i] += val
                i += i & -i
        print(self.tree)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        val1 = self._nums[i]
        index = i
        i = i + 1
        while i < len(self.tree):
            self.tree[i] = self.tree[i] - val1 + val
            i += i & -i
        self._nums[index] = val
        print(self.tree)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        j = j +1
        # both i and j are inclusion, so sum1 = sum(nums[:i]), sum2 = sum(nums[:j+1])
        while i > 0:
            sum1 += self.tree[i]
            i -= i & -i
        while j > 0:
            sum2 += self.tree[j]
            j -= j & -j
        return sum2-sum1
        

def main():
    obj = NumArray([1,3,5])
    x = obj.sumRange(0, 2)
    print(x)
    obj.update(1, 2)
    x = obj.sumRange(0, 2)
    print(x)

if __name__ == '__main__':
    main()