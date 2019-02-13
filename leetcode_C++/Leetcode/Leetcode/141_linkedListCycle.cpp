// 2019-02-13: pass, use hash table (set)

class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::set<ListNode *> nodeset;
        
        while (head) {
            if (nodeset.find(head) != nodeset.end()){
                return true;
            }else {
                nodeset.insert(head);
                head = head->next;
            }
        }
        return false;
    }
};

// use two pointer, one slow, one fast, see if two will met
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL) return false;
        auto slow = head, fast = head;
        while(fast != NULL && fast -> next != NULL){
            slow = slow -> next;
            fast = fast -> next -> next;
            if(slow == fast) return true;
        }
        return false;
        
    }
};