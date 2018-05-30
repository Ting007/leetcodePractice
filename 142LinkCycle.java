public class Solution {
    public ListNode detectCycle(ListNode head){
    	if (head == null) return head;
    	ListNode cur = head;
    	ListNode fast = head.next;
    	while(fast != null && fast.next != null){
    		if (fast == cur){//loop size measure
    			fast = fast.next;
    			int loopSize = 1;
    			while(fast!=cur){
    				fast=fast.next;
    				loopSize++;
    			}
    			fast = head;
    			cur = head;
    			for ( int i = loopSize; i > 0; i--){
    				fast = fast.next;
    			}
    			while(cur != fast){
    				cur = cur.next;
    				fast = fast.next;
    			}
    			return cur;
    		}
    		fast = fast.next.next;
    		cur = cur.next;
    	}

    	return null;
    }
}