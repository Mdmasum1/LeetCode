
#With the class create hash table constructor with the hash method

class HashTable:

    #Constructor
    def __init__(self, size= 7):
        #Initialize the NOne for the size of hash table
        self.data_map = [None] * size

    #Implement hash method
    def _hash(self, key):
        my_hash = 0

        #Looping throuhg the key
        for letter in key:
            #Calculation of the hash fucntion  using ord function and prime number
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        #return the hash
        return my_hash
    
    #implement print method
    def print_table(self):
        #Looping thriuhg the data map
        for i,val in enumerate(self.data_map):
            print(i, ": ", val)



my_hash_table = HashTable()
my_hash_table.print_table()


    
