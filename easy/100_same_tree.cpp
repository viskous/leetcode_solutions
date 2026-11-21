/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void inorder(vector<int> &ans, TreeNode* root){
        if (root == NULL){
            ans.push_back(-1);
            return;
        } 

        inorder(ans, root->left);
        ans.push_back(root->val);
        inorder(ans, root->right);
        
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<int> ans1;
        vector<int> ans0;
        inorder(ans1, p);
        inorder(ans0, q);
        return (ans1 == ans0);

    }
};