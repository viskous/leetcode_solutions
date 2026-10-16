/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        stack<int> s;
        if (head != NULL){
            s.push(slow->val);
        }

        while (fast != NULL && fast->next != NULL){
            slow = slow->next;
            s.push(slow->val);
            fast = fast->next->next;
        }
        s.pop();
        if (fast == NULL){
            while (slow != NULL){
                if (slow->val == s.top()){
                    s.pop();
                }
                slow = slow->next;
            }
        }
        else{
            slow = slow->next;
            while (slow != NULL){
                if (slow->val == s.top()){
                    s.pop();
                }
                slow = slow->next;
            }
        }
        return s.empty();
    }
};