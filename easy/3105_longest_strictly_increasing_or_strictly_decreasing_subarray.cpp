class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int inc = 1, dec = 1, t_inc = 1, t_dec = 1;
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] > nums[i-1]){
                t_inc += 1;
                if (t_inc > inc){
                    inc = t_inc;
                }
            } else {
                t_inc = 1;
            }
            if (nums[i] < nums[i-1]){
                t_dec += 1;
                if (t_dec > dec){
                    dec = t_dec;
                }
            } else {
                t_dec = 1;
            }
        }
        if (inc > dec) { return inc;}
        else{ return dec; }
    }
};