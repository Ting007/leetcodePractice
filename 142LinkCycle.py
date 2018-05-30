# Definition for singly-linked list.
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
        fast = head.next
        while fast != None and fast.next != None:
        	if(fast == cur):
        		fast=fast.next
        		loopSize = 1
        		while (fast != cur):
        			fast = fast.next
        			loopSize+=1
        		fast = head
        		cur = head
        		for i in range(loopSize):
        			fast = fast.next

        		while cur != fast:
        			cur=cur.next
        			fast=fast.next
        		return cur
        	fast = fast.next.next
        	cur = cur.next
        return None