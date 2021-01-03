
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
        for index, element in enumerate(self.arr[my_hash]):
            if len(element) == 2 and element[0] == key:         # Check if the particular key is already within the list
                self.arr[my_hash][index] = (key, value) 
        else:
            self.arr[my_hash].append((key, value)) # Appends the key value pair as a tuple (immutable)
        

    def __getitem__(self, key):
        my_hash = self.get_hash(key)
        for element in self.arr[my_hash]:
            if element[0] == key:
                return element[1]
            else:
                print("Key is not found!")


    def __delitem__(self, key):
        my_hash = self.get_hash(key)
        for index, element in enumerate(self.arr[my_hash]):
            if element[0] == key:
                del self.arr[my_hash][index]

        #### My attempt #####
        # for element in self.arr[my_hash]:
        #     if element[0] == key:
        #         del element
        #     else:
        #         print("Key is not found!")


# Initializing the HashTable class
t = HashTable()

# Simulating collision
print(t.get_hash("march 6"))
print(t.get_hash("58"))

t["march 6"] = 69
t["58"] = 120

print(t.arr)
# print(t["march 6"]) # The value gets overwritten due to a collision in the keys
print(t["march 6"])
del (t["march 6"])
print(t["58"])