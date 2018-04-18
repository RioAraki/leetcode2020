#include <iostream>
#include <vector>
// stack implementation, easiest way, no dynamic, no pointer
//# define MAX 1000;

// dynamic, generic
template<typename T>
class better_stack {
private:
	int m_top;
	const int MAX = 1000;
	std::vector<T> m_Array;
public:
	better_stack() {
		m_top = -1;
	}
	bool push(T x) {
		if (m_top == MAX) {
			return false;
		}
		else {
			m_Array.push_back(x);
			++m_top;
			return true;
		}
	}

	T pop() {
		if (m_top < 0) {
			return false;
		}
		else {
			T result = m_Array.back();
			m_Array.pop_back();
			return result;

		}
	}
	bool isEmpty() {
		return (m_top == -1);
	}
};

int main() {
	better_stack<char> stack;
	std::cout << stack.push('a') << std::endl;
	std::cout << stack.push('b') << std::endl;
	std::cout << stack.pop() << std::endl;
	std::cout << stack.pop() << std::endl;
	std::cout << stack.isEmpty() << std::endl;
	std::cin.get();

}


