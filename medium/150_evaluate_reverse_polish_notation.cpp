class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int a, b;
        for (string ch : tokens){
            if (ch == "+" || ch == "-" || ch == "*" || ch == "/"){
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                switch(ch[0]){
                    case '+':
                        st.push(a+b);
                        break;
                    case '-':
                        st.push(a-b);
                        break;
                    case '/':
                        st.push(a/b);
                        break;
                    case '*':
                        st.push(a*b);
                        break;
                }
            } else{
                st.push(stoi(ch));
            }
        }
        return st.top();
    }
};