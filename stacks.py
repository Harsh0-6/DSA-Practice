# Implementing Stack Data Structure.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
    
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if self.is_empty():
#             return None
#         popped_node = self.top
#         self.top = self.top.next
#         return popped_node.data

#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.top.data
    
#     def is_empty(self):
#         return self.top is None
    
#     def __len__(self):
#         current = self.top
#         count = 0
#         while current:
#             count += 1
#             current = current.next
#         return count
    
#     def print(self):
#         curr_node = self.top
#         while curr_node:
#             print(curr_node.data,end="->" )
#             curr_node = curr_node.next


# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     stack.push(4)
#     stack.push(5)

#     print("Top of the stack: ", stack.peek())
#     print("Size of the stack: ", len(stack))

#     print("Removing last element: ", stack.pop())
#     print(stack.print())

# -----------------------------------------------------------------        
# Implementing queue data structure.

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node  # front and rear point to the new node.
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_node = self.front  # Get the front node
        self.front = self.front.next

        if self.front is None: # If the queue becomes empty
            self.rear = None  # Update rear to None
        return dequeued_node.data  # Return the data of the dequeued node
    
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        count = 0
        current = self.front
        while current:
            current += 1
            current = current.next
        return count

    def __str__(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return "Queue: " + " ->".join(map(str, elements))
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue)
    print("first element: ", queue.peek())
    print("queue size: ", queue.size())

    print("Dequeue element: ", queue.dequeue())
    print(queue)

    print("new first element: ", queue.peek())
    print("new size: ", queue.size())