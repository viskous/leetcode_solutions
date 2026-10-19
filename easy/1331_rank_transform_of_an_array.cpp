class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> s = arr;
        sort(s.begin(), s.end());
        s.erase(unique(s.begin(), s.end()), s.end());

        for (int &x : arr)
            x = lower_bound(s.begin(), s.end(), x) - s.begin() + 1;
        return arr;
    }
};