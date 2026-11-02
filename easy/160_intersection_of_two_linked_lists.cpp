/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 #include<algorithm>
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        vector<ListNode*> v;
        ListNode* temp = headA;
        while (temp  != NULL){
            v.push_back(temp);
            temp = temp->next;
        }
        ListNode* temp1 = headB;
        while (temp1 != NULL) {
            if (find(v.begin(), v.end(), temp1) != v.end()) {
                return temp1;
            }
            temp1 = temp1->next;
        }
        return NULL;
    }
};