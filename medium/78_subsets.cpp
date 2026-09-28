class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> ans;
        vector<vector<int>> res;
        sets(nums, ans, res, 0);
        return res;
    }
    void sets(vector<int> &nums, vector<int> &ans, vector<vector<int>> &res, int i){
        if (i == nums.size()){
            res.push_back(ans);
            return;
        }
        ans.push_back(nums[i]);
        sets(nums, ans, res, i+1);

        ans.pop_back();
        sets(nums, ans, res, i+1);
    }
};