class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        set<vector<int>> us;
        vector<int> res;
        getAllSubsets(nums, res, us, 0);
        return vector<vector<int>>(us.begin(), us.end());
    }
    void getAllSubsets(vector<int> &nums, vector<int> &res, set<vector<int>> &us, int i){
        if (i == nums.size()){
            us.insert(res);
            return;
        }
        res.push_back(nums[i]);
        getAllSubsets(nums, res, us, i+1);

        res.pop_back();
        getAllSubsets(nums, res, us, i+1);
    }
};