class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        unordered_map<char, char> hash_map = {
        {')','('},
        {']','['},
        {'}','{'}};
        for (char ch : s){
            if (hash_map.count(ch)){
                if (st.empty() || st.top() != hash_map[ch]) return false;
                st.pop();
            }
            else{
                st.push(ch);
            }
        }
        return st.empty();
    }
};