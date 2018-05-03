#include <iostream>
#include <vector>
// stack implementation, easiest way, no dynamic, no pointer
//# define MAX 1000;

// dynamic, generic
// since vector is dynamic array, does not need to have max

#define TABLE_SIZE 10

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



template<typename T>
struct Node {
	int key;
	T value;
	Node* next = NULL;
	Node* prev = NULL;
	Node(int key, int value) {
		this->value = value;
		this->key = key;
	};
};

template<typename T>
class Linkedlist {

	Node<T>* head;
	Node<T>* tail;

public:
	Linkedlist() {
		head = NULL;
	}

	void LinkInsert(Node<T> x) {
		x.next = head;
		if (head != NULL) {
			head->prev = &x;
		}
		head = &x;
	}

	Node<T> LinkSearch(int k) {
		Node<T>* x = head;
		while (x != NULL && x->key != k) {
			x = x->next;
		}
		return *x;
	}

	void LinkDelete(Node<T> x) {
		int key = x.key;
		Node<T> del_node = LinkSearch(key);
		if (del_node.prev != NULL) {
			(del_node.prev)->next = del_node.next;
		}
		else {
			head = del_node.next;
		}
		if (del_node.next != NULL) {
			(del_node.next)->prev = del_node.prev;
		}
	}

	void print() {
		Node<T>* x = head;
		while (x != NULL) {
			std::cout << x->key << ' ' << x->value << " -> ";
			x = x->next;
		}
		std::cout << std::endl;

	}

};

// hashnode works like linked list in terms of data structure, except it does not need to support operations like insert and search
template<typename K, typename V>
class HashNode {
private:
	K key;
	V value;
	HashNode* next;
public:
	HashNode(K &key, V &value):
		key(key), value(value), next(NULL) {
	}

	K getKey() const {
		return key;
	}

	V getValue() const{
		return value;
	}

	HashNode* getNext() const {
		return next;
	}

	// key is get by hashfunction
	void setKey(K key) {
		this.key = key;
	}

	void setValue(V value) {
		this.value = value;
	}

	void setNext(HashNode* next) {
		this->next = next;
	}
};

template <typename K>
struct KeyHash {
	unsigned long operator()(const K& key) const {
		return reinterpret_cast<unsigned long>(key) % TABLE_SIZE;
	}
};


// The hashtable class support various hash function, generic insert input (must be same type, here we ue char and int) and 
// The input must come along with a key and value (which is not always the case)
// TODO: we could generate a key in long type given a value

template<typename K, typename V, typename F = KeyHash<K>>
class HashTable {
private:
	HashNode<K, V> **table;
	F hashFunc;
public:
	HashTable() {
		table = new HashNode<K,V> *[TABLE_SIZE]();
	}

	~HashTable() {
		for (int i =0; i < TABLE_SIZE; ++i) {
			HashNode<K, V> *entry = table[i];
			while (entry != NULL) {
				HashNode<K, V> *prev = entry; // prev points to table[i] not entry
				entry = entry->getNext(); // change entry does not affect prev
				delete prev;
			}
			table[i] == NULL; // reassign back to null
		}

		delete[] table;
	}

	bool HashSearch(const K &key, V &value) {
		unsigned long hashValue = hashFunc(key);
		HashNode<K, V>* entry = table[hashValue];

		while (entry != NULL) {
			if (entry->getKey() == key && entry->getValue() == value){
				return true;
			}
			entry = entry->getNext();
		}
		return false;
	}

	void HashInsert(const K &key, V &value) {
		unsigned long hashValue = hashFunc(key);
		HashNode<K, V>* entry = table[hashValue];
		HashNode<K, V>* prev = NULL;

		while (entry != NULL && entry->getKey() != key) {
			prev = entry;
			entry = entry->getNext();
		}

		if (entry == NULL) {
			entry = new HashNode<K, V>(key, value);
			if (prev == NULL) {
				table[hashValue] = entry;
			}
			else {
				prev->setNext(entry);
			}
		}
		else { // update the value
			entry->setValue(value);
		}
	}

	void remove(const K &key) {
		unsigned long hashValue = hashFunc(key);
		HashNode<K, V> *prev = NULL;
		HashNode<K, V> *entry = table[hashValue];

		while (entry != NULL && entry->getKey() != key) {
			prev = entry;
			entry = entry->getNext();
		}

		if (entry == NULL) {
			// key not found
			return;
		}
		else {
			if (prev == NULL) {
				// remove first bucket of the list
				table[hashValue] = entry->getNext();
			}
			else {
				prev->setNext(entry->getNext());
			}
			delete entry;
		}
	}

};


int main() {

	// test linked list

	Node<char> a = Node<char>(1, 'a');
	Node<char> b = Node<char>(5, 'b');
	Node<char> c = Node<char>(2, 'c');

	Linkedlist<char> ll;

	ll.LinkInsert(a);
	ll.LinkInsert(b);
	ll.LinkInsert(c);
	ll.print();
	ll.LinkSearch(5);
	ll.LinkDelete(c);
	ll.print();

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
	//Queue<char> queue;
	//
	//queue.Enqueue('a');
	//queue.Enqueue('b');
	//queue.Enqueue('c');
	//queue.Enqueue('d');
	//queue.Dequeue();
	//queue.Enqueue('e');
	//queue.Enqueue('f');
	//queue.Enqueue('g');
	//queue.info();
	std::cin.get();



}


