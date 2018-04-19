#include <iostream>
#include <vector>
// stack implementation, easiest way, no dynamic, no pointer
//# define MAX 1000;

// dynamic, generic
// since vector is dynamic array, does not need to have max
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


template<typename T>
class Queue {
private:
	int m_head, m_tail;
	const static int MAX = 5;
	T m_array[MAX] = { NULL };
public:
	Queue() {
		m_head = -1;
		m_tail = -1;
	}

	bool CheckEmpty() {
		return (m_head == -1 && m_tail == -1);
	}

	//if queue is full, tail would be either one slot before head or tail at the last slot, head at the first slot
	bool CheckFull() {
		return (m_tail + 1 == m_head) or (m_tail == MAX && m_head == 0);
	}

	void Enqueue(T x) {
		if (CheckEmpty()) {
			m_head = 0;
			m_tail = 0;
			m_array[0] = x;
		}
		else {
			if (!CheckFull()) {
				++m_tail;
				if (m_tail > MAX - 1) {
					m_tail = 0;
				}
				m_array[m_tail] = x;
			}
			else {
				std::cout << "Queue already full" << std::endl;
			}
		}
		
	}

	void Dequeue() {
		if (!CheckEmpty()) {
			m_array[m_head] = NULL;
			++m_head;
			if (m_head > MAX - 1) {
				m_head = 0;
			}
		}
		else {
			std::cout << "Queue already empty" << std::endl;
		}
	}

	int count() {
		int count = m_tail - m_head + 1;
		if (m_tail == -1 && m_head == -1) {
			count = 0;
		}
		else if (m_tail < m_head) {
			count = m_tail + MAX - m_head + 1;
		}
		return count;
	}

	void info() {

		std::cout << "There are " << count() << " elements in the queue." << std::endl;
		for (T element : m_array) {
			if (element == NULL) {
				std::cout << "EMPTY" << " ";
			}
			std::cout << element << " ";
		}
		std::cout << std::endl;
		//std::cout << m_array << std::endl;

	}
};


int main() {
	// test stack
	/*better_stack<char> stack;
	std::cout << stack.push('a') << std::endl;
	std::cout << stack.push('b') << std::endl;
	std::cout << stack.pop() << std::endl;
	std::cout << stack.pop() << std::endl;
	std::cout << stack.isEmpty() << std::endl;
	std::cin.get();*/

	// test queue

	// test linked list
	Queue<char> queue;

	
	queue.Enqueue('a');
	queue.Enqueue('b');
	queue.Enqueue('c');
	queue.Enqueue('d');
	queue.Dequeue();
	queue.Enqueue('e');
	queue.Enqueue('f');
	queue.Enqueue('g');
	queue.info();
	std::cin.get();
}


