class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res;
        int l = 0;
        int n = nums.size();
        int r = n-1;
        bool flag1 = false;
        bool flag2 = false;
        while (l < n){
            if (nums[l] == target && flag1 == false){
                res.push_back(l);
                flag1 = true;
            }
            if (nums[r] == target && flag2 == false){
                res.push_back(r);
                flag2 = true;
            }
            if (flag1 == true && flag2 == true){
                sort(res.begin(), res.end());
                return res;
            }
            l++;
            r--;
        }
        res.push_back(-1);
        res.push_back(-1);
        return res;
    }
};