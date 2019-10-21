#!/usr/bin/env python3
"""
:author:    Murtaza Hatim 
:date:      16/10/2019
"""

class HashTable:
    '''
    This class represents a hash table
    '''
    def __init__(self, table_capacity = 1103, hash_base = 29): 
        '''
        This function initializes all the instance variables of this class
        @complexity:    Best Case: O(1) / Worst Case: O(1)
        @input:         table_capacity: size of table
                        hash_base: base value of the hash function
        @return:        None
        '''
        self.table = [None] * table_capacity
        self.base = hash_base
        self.table_size = table_capacity;
        self.count = 0
  
    def __getitem__(self, key):
        '''
        This function allows a user to access a value from the hash table using the key
        @complexity:    Best Case: O(1) / Worst Case: O(table_size)
        @input:         key: key from the key value pairs stored in the Hash Table
        @return:        value corresponding to the input key
        @pre-condition: input key should be valid    
        '''

        if not isinstance(key, str):
            raise TypeError("Key is not a String")

        # Calling the hash function to hash the key
        pos = self.hash(key)

        for _ in range (self.table_size):
            # If that key does not exist in the table
            if self.table[pos] is None:
                raise KeyError("key not found")
                return
            # if key exits at hashed position
            elif self.table[pos][0] == key:
                return self.table[pos][1]
            else:
                pos = (pos + 1) % self.table_size

        raise KeyError("key not found")

    def __setitem__(self, key, value):
        '''
        This function allows the user to set the value corresponding to a key
        @complexity:    Best Case: O(1) / Worst Case: O(table_size)
        @input:         key: key from the key value pairs stored in the Hash Table
                        value: value to be set for input key
        @return:        None
        '''

        if not isinstance(key, str):
            raise TypeError("Key is not a String")

        # Calling the hash function to hash the key
        pos = self.hash(key)
        
        for _ in range (self.table_size):
            # If that key does not exist in the table
            if self.table[pos] is None:
                self.table[pos]=(key, value)
                self.count += 1
                return
            # if key exits at hashed position
            elif self.table[pos][0] == key:
                self.table[pos]=(key, value)
                return
            else:
                pos = (pos + 1) % self.table_size

        self.table = self.rehash()
        self.__setitem__(key, value)
        
       
    def __contains__(self, key):
        '''
        This function returns if key exists in table or not
        @complexity:    Best Case: O(1) / Worst Case: O(table_size)
        @input:         key: key from the key value pairs stored in the Hash Table
        @returns:       True if key exists in Hash table, False otherwise
        '''
        if not isinstance(key, str):
            raise TypeError("Key is not a String")

        pos = self.hash(key)

        for _ in range (self.table_size):
            if self.table[pos] is None:
                return False
            elif self.table[pos][0] == key:
                return True
            else:
                pos = (pos + 1) % self.table_size
        
        return False

    def hash(self, key):
        '''
        This function hashes a String Key to an index value in the table
        @complexity:    Best Case: O(N) / Worst Case: O(N) where N is the length of the key string
        @input:         key: key from the key value pairs stored in the Hash Table
        @returns:       value: index (integer) value of the String
        '''
        value = 0
        for i in range(len(key)):
            value = ((value * self.base) + ord(key[i])) % self.table_size
        return value

    def rehash(self):
        '''
        This function creates a new hash table of larger size
        @complexity:    Best Case: O(N) / Worst Case: O(NM) where N is the length of the original table 
                        and M is the length of the new table
        @input:         None
        @returns:       new hash table
        '''

        # List of prime numbers to set new table size
        prime_numbers = [ 3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 
                         293, 353, 431, 521, 631, 761, 919, 1103, 1327, 1597, 1931, 2333, 2801, 
                         3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591, 17519, 21023, 
                         25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 
                         156437, 187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 
                         807403, 968897, 1162687, 1395263, 1674319, 2009191, 2411033, 2893249, 
                         3471899, 4166287, 4999559, 5999471, 7199369]

        new_table_size = 0

        for prime_index in range(len(prime_numbers) - 1):
            if prime_numbers[prime_index] < 2 * self.table_size and \
            prime_numbers[prime_index + 1] >= self.table_size:
                new_table_size = prime_numbers[prime_index + 1]
                break

        if new_table_size == 0:
            raise ValueError("Table could not be rehashed")

        self.table_size = new_table_size
        new_table = [None] * self.table_size
        
        # Rehashing keys into new table
        for tuple in self.table:
            if tuple is not None:
                pos = self.hash(tuple[0])
                for i in range (self.table_size):
                    if new_table[pos] is None:
                        new_table[pos]=(tuple[0], tuple[1])
                        break
                    elif new_table[pos][0] == tuple[0]:
                        new_table[pos]=(tuple[0], tuple[1])
                        break
                    else:
                        pos = (pos + 1) % self.table_size 


        return new_table


                               
