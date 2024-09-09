# Arrays = Lists in python.

nums = [1, 2, 3, 4]
for i in range(len(nums)):
    print(nums[i])

#  2d Array
nums1 = [[1, 2, 3], [4, 5, 6]]
for i in range(len(nums1)):
    for j in range(len(nums1[i])):
        print([j])

#  Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    # Initialize the head of the list.

#  method for addding data at the end.
    def append(self, data):
        new_node = Node(data)
        if not self.head:   # if the list is empty.
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # traversing to the last.
            last_node = last_node.next
        last_node.next = new_node  # adding the new to last node.

# method for deleting the first occerunce of data.
    def delete(self, key):
        current_node = self.head
        previous_node = None
        # check if the head node itself holds the key.
        if current_node and current_node.data == key:
            self.head = current_node.next    #change head
            current_node = None
            return
        # search for the key to be deleted.
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next

        # if the key is not in the linked list.
        if not current_node:
            print("Node with the data {key} not found.")
            return
        
        # unlink the node from the linked list.
        previous_node.next = current_node.next
        current_node = None       # free the memeory

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")   # indicates the end of the list.

# creating the linked list.
linkedlist = LinkedList()

# adding node to the list.
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)

# displaying elements.
print("linked list")
linkedlist.display()

# deleting elements.
linkedlist.delete(3)
linkedlist.delete(4)
linkedlist.display()