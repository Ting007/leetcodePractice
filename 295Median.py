from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowHeap=[]
        self.highHeap=[]
        self.median = None
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.median == None:
            heappush(self.lowHeap, -num)
            self.median = num
        else:
            if num <= self.median:
                if len(self.lowHeap) <= len(self.highHeap):
                    heappush(self.lowHeap, -num)
                else:
                    shift = heappop(self.lowHeap)
                    heappush(self.highHeap, -shift)
                    heappush(self.lowHeap, -num)
            if num > self.median:
                if len(self.highHeap) <= len(self.lowHeap):
                    heappush(self.highHeap, num)
                else:
                    shift=heappop(self.highHeap)
                    heappush(self.highHeap, num)
                    heappush(self.lowHeap, -shift)
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lowHeap) == 0 and len(self.highHeap) == 0:
            return self.median
        elif len(self.lowHeap) == len(self.highHeap):
            self.median = float((-self.lowHeap[0]) + self.highHeap[0])/2.0
        elif len(self.lowHeap) > len(self.highHeap):
            self.median = float(-self.lowHeap[0])
        else:
            self.median = float(self.highHeap[0])
        return self.median

def main():
        foo = MedianFinder()
        nums = [1,2,3,4,5,6,7,8,9,10]
        for i in range(len(nums)):
            foo.addNum(nums[i])
            print(foo.findMedian())

if __name__ == "__main__":
        main()