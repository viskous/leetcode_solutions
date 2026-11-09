class MinStack {
    stack<int> st;
    stack<int> minst;
public:
    MinStack() {
        
    }
    
    void push(int value) {
        if (minst.empty() || value <= minst.top()){
            minst.push(value);
        }
        st.push(value);
    }
    
    void pop() {
        if (st.top() == minst.top()){
            minst.pop();
        }
        return st.pop();
        
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return minst.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */