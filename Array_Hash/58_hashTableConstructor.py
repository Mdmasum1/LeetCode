
#With the class create hash table constructor with the hash method

class HashTable:

    #NB: Prime number increases the randomness of the key-val pair. It is better 
    # remove the prime number from the end reducing collision

    #Constructor
    def __init__(self, size= 7):
        #Initialize data_map variable to None for the size of hash table
        self.data_map = [None] * size

    #Implement hash method
    def _hash(self, key):
        #create my_hash variable set to 0
        my_hash = 0

        #Looping throuhg the key
        for letter in key:
            #Calculation of the hash fucntion  using ord function and multiply prime number
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        #return the hash
        return my_hash
    
    #implement print method
    def print_table(self):
        #Looping thriuhg the data map
        for i,val in enumerate(self.data_map):
            print(i, ": ", val)

    #implemet set_item method
    def set_item(self, key, value):
        #Initialize index variable and set to hash function
        index = self._hash(key)

        #Checking if it is none, then index set to empty list
        if self.data_map[index] == None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])


    #Implementation of get_item method
    def get_item(self, key):
        #initialize variable index and set to hash function set to key
        index = self._hash(key)

        #Checking it is in the input array
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):

                if self.data_map[index][i][0] == key:

                   return self.data_map[index][i][1]
            
        return None

        


my_hash_table = HashTable()

my_hash_table.set_item('mango', [])
my_hash_table.set_item('apple', 100)
my_hash_table.set_item('lemon', 50)

print(my_hash_table.get_item('mango'))
print(my_hash_table.get_item('apple'))
print(my_hash_table.get_item('lemon'))


#my_hash_table.print_table()


    
