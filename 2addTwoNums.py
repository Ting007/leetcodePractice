#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:	
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nlist=ListNode(0)
        carry = 0 
        add = l1.val + l2.val + carry
        if add >= 10:
            temp = divmod(add, 10)
            remainder = temp[1]
            carry = temp[0]
            digit = ListNode(remainder)
        else:
            digit = ListNode(add)
        nlist.next=digit
        while l1.next != None or l2.next != None or carry != 0:
            if l1.next == None and l2.next == None:
                l1.val = 0
                l2.val = 0
            elif l1.next == None:
                l1.val = 0
                l2=l2.next
            elif l2.next ==None:
                l2.val = 0
                l1=l1.next
            else:
                l1=l1.next
                l2=l2.next
            add = l1.val + l2.val + carry
            if add >= 10:
                temp = divmod(add, 10)
                remainder = temp[1]
                carry = temp[0]
                newNode = ListNode(remainder)
            else:
                newNode = ListNode(add)   
                carry = 0 
            digit.next=newNode
            digit=digit.next
        return nlist.next

def main():
        foo = Solution()
        S=[2,3,4]
        C=[4,5,6]
        foo.addTwoNumbers(S, C)

if __name__ == "__main__":
        main()



