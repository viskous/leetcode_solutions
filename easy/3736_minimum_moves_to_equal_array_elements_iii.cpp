class Solution {
public:
    int minMoves(vector<int>& nums) {
        int count = 0;
        int max = *max_element(nums.begin(), nums.end());
        for ( int i : nums){
            count += max - i;
        }
        return count;
    }
};