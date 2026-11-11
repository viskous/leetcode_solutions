class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans;
        int n = temperatures.size();
        int count = 0;
        bool flag = false;
        for (int i = 0; i < n; i++){
            flag = false;
            for (int j = i; j < n; j++){
                if ( temperatures[j] > temperatures[i]){
                    ans.push_back(count);
                    flag = true;
                    break;
                } else {
                    count += 1;
                }
            }
            if (flag == false){
                ans.push_back(0);
            }
            count = 0;
        }
        return ans;
    }
};