class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        cur = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            cur = cur.next
            if(fast == cur):
                cur=head
                break
        if fast == None or fast.next == None:
            return None
        while cur != fast:
            cur=cur.next
            fast=fast.next
        return cur