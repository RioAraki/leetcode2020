/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode prev = new ListNode(0);
        ListNode head = prev;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            
            int l1v = 0;
            if (l1 != null) {
                l1v = l1.val;
                l1 = l1.next;
            }
            int l2v = 0;
            if (l2 != null) {
                l2v = l2.val;
                l2 = l2.next;
            }
            int sum = l1v + l2v + carry;
            carry = 0;
            if (sum > 9) {
                sum -= 10;
                carry = 1;
            }
            head.next = new ListNode(sum);        
            head = head.next;
        }
        
        return prev.next;
    }
}