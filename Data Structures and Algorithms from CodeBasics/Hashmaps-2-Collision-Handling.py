
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[]for i in range(self.MAX)] # You have to initialize an empty array now, since each memory location is a linked list with a key value pair

    # Defining a hash function
    def get_hash(self, key):
        h = 0 
        for char in key:
            h += ord(char) # The ord method finds the relevant ASCII value for a given character 
        return h % 100

    # def add(self, key, value):
    #     my_hash = self.get_hash(key) # Converts a given key into an integer value
    #     self.arr[my_hash] = value # Sets that integer value to a location on the predefined array. This allows for retrieval of that data later on.

    # def get(self, key):
    #     my_hash = self.get_hash(key)
    #     return self.arr[my_hash]

    ## Implementing Operator Overloading to allow [] for use
    def __setitem__(self, key, value):
        my_hash = self.get_hash(key) # Converts a given key into an integer value
        self.arr[my_hash] = value # Sets that integer value to a location on the predefined array. This allows for retrieval of that data later on.

    def __getitem__(self, key):
        my_hash = self.get_hash(key)
        return self.arr[my_hash]

    def __delitem__(self, key):
        my_hash = self.get_hash(key)
        self.arr[my_hash] = None       


# Initializing the HashTable class
t = HashTable()

# Simulating collision
print(t.get_hash("march 6"))
print(t.get_hash("april 1"))