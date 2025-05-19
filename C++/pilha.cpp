#include <iostream>
#include <stack>

int main() {
    std::stack<int> s;
    s.push(1);
    s.push(2);
    std::cout << "Pop: " << s.top() << "\n";
    s.pop();
    return 0;
}