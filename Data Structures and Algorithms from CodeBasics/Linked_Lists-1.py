class Node:
    def __init__(self, data = None, next = None): # The "next = None" parameter is a pointer to the next element
        self.next = next
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head) # "self.head" is the "next" argument in the Node class; it shifts the pointer to the first node in the linked list
        self.head = node # Overrides the empty self.head at the __init__ for the LinkedList class

    def print(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        else:
            itr = self.head # Initializing the iterator to iterate through the linked list
            liststr = ""
            while itr:
                liststr += str(itr.data) + "-->"
                itr = itr.next # Moves to the next node in the linked list
            print(liststr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None) # The pointer is now on self.head. The "next = None argument" represents the pointer pointing at nothing (end of the linked list)
            return
        else:
            itr = self.head
            while itr.next: # If itr.next has some value, you are not at the end of the linked list. Keep iterating.
                itr = itr.next
            itr.next = Node(data, None) # You have reached the last element. The pointer is pointing towards None (end of the linked list)

    def insert_values(self, data_list):
        self.head = None # Removing all the current values 
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length(): # Checking for out of range operations
            raise Exception ("Invalid Index!")

        if index == 0:
            self.head = self.head.next # Points to the next element
            return 
        else:
            count = 0 
            itr = self.head
            while itr: 
                if count == index-1 : # You have to manipulate the link of the node that is before your target node (to be deleted)
                    itr.next = itr.next.next # Skips the node that is to be deleted
                    break
                itr = itr.next
                count += 1 

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length(): # Checking for out of range operations
            raise Exception ("Invalid Index!")
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1: # When inserting an item into a linked list, you want to target the link that is connecting the previous node of your target insertion point
                    node = Node(data, itr.next) # itr.next refers to the next node of this newly inserted element
                    itr.next = node
                    break
                itr = itr.next
                count += 1 


# Question 1: Implement two functions that :
    # 1) Does a lookup by value, and inserts a new node after that lookup node
    # 2) Does a lookup by value and removes the first node that contains that value

    def insert_after_value(self, data_after, data_to_insert):
        count = 0 
        itr = self.head
        while itr:
            if itr == data_after:
                node = Node(data_to_insert, data_after.next)
                itr.next = node
                break
            itr = itr.next 
            count += 1



                    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(2)
    ll.insert_at_end(10)
    ll.insert_after_value(10, 7)
    ll.print()