/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0), cur = dummy;
        dummy.next = head;
        int prefix = 0;
        
        // hashmap to take prefix sum as a key,  related node as the value
        Map<Integer, ListNode> m = new HashMap<>();
        
        // scan the linked list, accumulate the node's value as prefix sum
        //   1. if prefix is never seen, set m[prefix] = cur
        //   2. if prefix seen before, m[prefix] is the node we achieve this prefix sum,
        //      skip (delete) all nodes between m[prefix] and cur.next
        
        // eg: 1 2 3 -2 -3
        // pf: 1 3 5 3  1
        
        while (cur != null) {
            prefix += cur.val;
            if (m.containsKey(prefix)) {
                cur = m.get(prefix).next;
                int p = prefix + cur.val;
                while (p != prefix) {
                    m.remove(p);
                    cur = cur.next;
                    p += cur.val;
                }
                m.get(prefix).next = cur.next;
            } else {
                m.put(prefix, cur);
            }
            cur = cur.next;
            
        }
        return dummy.next;
        
    }
}