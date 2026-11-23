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
    void levelTraversal(vector<vector<int>> &res, vector<int> &ans, TreeNode* root){
        if (!root) return;
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        while(!q.empty()){
            TreeNode* node = q.front();
            q.pop();
            if (node == NULL){
                if (!q.empty()){
                    res.push_back(ans);
                    ans.clear();
                    q.push(NULL);
                    continue;
                } else {
                    res.push_back(ans);
                    break;
                }
            }

            ans.push_back(node->val);

            if (node->left != NULL){
                q.push(node->left);
            }
            if (node->right != NULL){
                q.push(node->right);
            }
        }
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<int> ans;
        vector<vector<int>> res;
        levelTraversal(res, ans, root);
        return res;

    }
};