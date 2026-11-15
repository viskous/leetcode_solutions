class Solution {
public:
    void combi(int start, int n, int k, vector<int>& ans, vector<vector<int>>& res) {
        if (ans.size() == k) {
            res.push_back(ans);
            return;
        }
        for (int i = start; i <= n; i++) {
            ans.push_back(i);
            combi(i + 1, n, k, ans, res);
            ans.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> ans;
        combi(1, n, k, ans, res);
        return res;
    }
};