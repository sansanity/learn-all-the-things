# Question 4: Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing.
# Keep MAX size of arr in hashtable as 10.


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)] # You have to initialize an empty array now, since each memory location is a linked list with a key value pair
        print(self.arr)
    # Defining a hash function
    def get_hash(self, key):
        h = 0 
        for char in key:
            h += ord(char) # The ord method finds the relevant ASCII value for a given character 
        return h % self.MAX

    def get_full_range(self, index):
        print([*range(index, len(self.arr))] + [*range(0, index)])
        return [*range(index, len(self.arr))] + [*range(0, index)] # Returns a list of integers in a list
        # From index to the end of self.arr
        # From 0 to the index

    def find_empty_slot(self, key, index):
        my_range = self.get_full_range(index)
        for index in my_range:
            if self.arr[index] == None: # If this is true, then the slot is already empty
                return index 
            elif self.arr[index][0] == key: # If there is a match in the keys (??)
                return index
            # elif self.arr[index]: # Optional for readability: elif condition to skip over an already populated node
            #     continue
        raise Exception("Hashmap is full!") # By not setting this as an else condition, the for loop will automatically skip through already populated nodes
 
    def __getitem__(self, key):
        my_hash = self.get_hash(key)
        if self.arr[my_hash] is None:
            return
        else:
            my_range = self.get_full_range(my_hash)
            for index in my_range: # Looking for the element by scanning through each item in self.arr
                element = self.arr[index]
                if element is None: # I don't understand why you would return upon finding a None, don't you want to keep searching/
                    return
                elif element[0] == key: # If there is a match in the key
                    return element[1]
                else:
                    raise Exception("Element is not in the hashmap!")
   
    def __setitem__(self, key, val):
        my_hash = self.get_hash(key)
        if self.arr[my_hash] is None:
            self.arr[my_hash] = (key, val) # Stores the key value pair here, since this slot is not taken
        else:
            new_hash = self.find_empty_slot(key, my_hash)
            self.arr[new_hash] = (key,val)
        print(self.arr)

    def __delitem__(self, key):
        my_hash = self.get_hash(key)
        my_range = self.get_full_range(my_hash)
        for index in my_range:
            if self.arr[index] is None:
                return # The item is not found, so you return
            if self.arr[index][0] == key:
                self.arr[index] = None # The item is found, so you delete the item by setting its slot to None
            print(self.arr)


# Initializing the HashTable class
t = HashTable()


t["march 6"] = 69
# t.get_full_range(9)
t["58"] = 120

# Simulating collision
print(t.get_hash("march 6"))
print(t.get_hash("58"))
print(t.arr)

