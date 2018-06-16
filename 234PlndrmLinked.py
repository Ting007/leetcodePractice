class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        first = []
        fast = head
        slow = head
        if head == None:
            return True
        while fast:
            first.append(slow)
            if fast.next != None:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        item = first.pop()
        while slow and slow.val == item.val:
            slow = slow.next
            if first != []:
                item = first.pop()
        if slow != None:
            return False
        return True