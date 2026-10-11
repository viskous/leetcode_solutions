/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool cycle(ListNode* slow, ListNode* fast){
        if (slow == NULL || fast == NULL || fast->next == NULL){
            return false;
        }
        if (fast == slow){
            return true;
        }
        slow = slow->next;
        fast = fast->next->next;
        return cycle(slow, fast);
    }
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        if (head == NULL){
            return false;
        }
        fast = fast->next;
        return cycle(slow, fast);
    }
};