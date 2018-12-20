// 2018-12-19: tuck on the syntax, need to review about pointer

// Definition for singly-linked list.
#define NULL nullptr
#include <vector>;
#include <unordered_map>
#include <stdio.h>;
#include <iostream>;


 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
  ListNode * addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode ret(0);
    ListNode* tmp = &ret;

    int extra = 0;
    while (l1 || l2 || extra) {
      int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + extra;
      extra = sum / 10;
      tmp->next = new ListNode(sum % 10);
      tmp = tmp->next;
      l1 = l1 ? l1->next : l1;
      l2 = l2 ? l2->next : l2;
    }
    return ret.next;
  }
};