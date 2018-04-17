

// stack implementation, easiest way, no dynamic, no pointer
//# define MAX 1000;


class Stack {
	int top;
	const static int MAX = 1000;
public:
	int array[MAX];
	
	Stack() {
		top = -1;
	};

	bool push(int x);
	int pop();
	bool isEmpty();
};

bool Stack::push(int x) {
	if (top >= MAX) {
		return false;
	} else {
		array[++top] = x;
		return true;
	}
}

int Stack::pop() {
	if (top == -1) {
		return 0; // what if we mess up with 0 stored in stack?
	}
	else {
		int x = array[top--];
		return x;
	}
}

bool Stack::isEmpty() {
	return top == -1;
}


// dynamic, generic
class better_stack {


};
