class Stack:
    """
    A simple Stack data structure implementation.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item from the stack.
        peek(): Return the top item without removing it.
        is_empty(): Check if the stack is empty.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.
        Returns:
            The top item if the stack is not empty.
            None if the stack is empty (edge case handled).
        """
        if self.is_empty():
            print("Warning: Attempt to pop from empty stack")
            return None
        return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.
        Returns:
            The top item if the stack is not empty.
            None if the stack is empty (edge case handled).
        """
        if self.is_empty():
            print("Warning: Attempt to peek from empty stack")
            return None
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, else False."""
        return len(self.items) == 0

# -------------------------------
# Testing the Stack class
# -------------------------------

stack = Stack()

# Test pushing
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.items)  # [10, 20, 30]

# Test peek
print("Peek:", stack.peek())  # 30

# Test popping
print("Pop:", stack.pop())  # 30
print("Pop:", stack.pop())  # 20
print("Pop:", stack.pop())  # 10
print("Pop from empty stack:", stack.pop())  # Warning + None

# Test peek on empty stack
print("Peek on empty stack:", stack.peek())  # Warning + None
