#!/usr/bin/env python3
"""
:author:    Murtaza Hatim 
:date:      20/10/2019
"""

import math
from timeit import default_timer
import csv


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
        self.collision_count = 0
        self.probe_total = 0
        self.probe_max = 0
        self.rehash_count = 0
  
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

        pos = self.hash(key)
        quadratic_counter = 0
        og_pos = pos

        for _ in range (self.table_size):
            if self.table[pos] is None:
                raise KeyError("key not found")
                return
            elif self.table[pos][0] == key:
                return self.table[pos][1]
            else:
                quadratic_counter += 1
                pos = og_pos
                pos = (pos + (quadratic_counter ** 2)) % self.table_size

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

        pos = self.hash(key)
        og_pos = pos
        collisionOccured = False
        probe_length = 0
        isSuccessful = False

        for _ in range (self.table_size):
            if self.table[pos] is None:
                self.table[pos]=(key, value)
                self.count += 1
                isSuccessful = True 
                break
            elif self.table[pos][0] == key:
                self.table[pos]=(key, value)
                isSuccessful = True 
                break
            else:
                if not collisionOccured:
                    self.collision_count += 1
                    collisionOccured = True
                probe_length += 1
                pos = og_pos
                pos = (pos + (probe_length ** 2)) % self.table_size
                
        self.probe_total += probe_length

        if self.probe_max < probe_length:
            self.probe_max = probe_length

        if not isSuccessful:
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
        quadratic_counter = 0
        og_pos = pos

        for _ in range (self.table_size):
            if self.table[pos] is None:
                return False
            elif self.table[pos][0] == key:
                return True
            else:
                quadratic_counter += 1
                pos = og_pos
                pos = (pos + (quadratic_counter ** 2)) % self.table_size
        
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

        self.rehash_count += 1
        prime_numbers = [ 3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 
                         293, 353, 431, 521, 631, 761, 919, 1103, 1327, 1597, 1931, 2333, 2801, 
                         3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591, 17519, 21023, 
                         25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 
                         156437, 187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 
                         807403, 968897, 1162687, 1395263, 1674319, 2009191, 2411033, 2893249, 
                         3471899, 4166287, 4999559, 5999471, 7199369]

        new_table_size = self.table_size * 2

        for prime_index in range(len(prime_numbers) - 1):
            if prime_numbers[prime_index] < new_table_size and \
            prime_numbers[prime_index + 1] >= new_table_size:
                new_table_size = prime_numbers[prime_index + 1]
                break

        self.table_size = new_table_size
        new_table = [None] * self.table_size

        for tuple in self.table:
            if tuple is not None:
                pos = self.hash(tuple[0])
                quadratic_counter = 0
                og_pos = pos
                for i in range (self.table_size):
                    if new_table[pos] is None:
                        new_table[pos]=(tuple[0], tuple[1])
                        break
                    elif new_table[pos][0] == tuple[0]:
                        new_table[pos]=(tuple[0], tuple[1])
                        break
                    else:
                        quadratic_counter += 1
                        pos = og_pos
                        pos = (pos + (quadratic_counter ** 2)) % self.table_size 

        return new_table
                               
    def statistics(self):
        '''
        This function returns a tuple of all the statistics required for the hash table
        @complexity:    O(1)
        @input:         None
        @return:       tuple; collision count, total probe length, max probe length, rehash count
        '''
        return self.collision_count, self.probe_total, self.probe_max, self.rehash_count


def load_dictionary(hash_table, filename, time_limit = math.inf):
    '''
    This function loads words from a file into a hash table
    @complexity:    Best Case: O(lines) / Worst Case: O(lines * table_size)
    @input:         hash_table: HashTable object
                    filename: Name of file for lines to be added
                    time_limit: maximum allowed time limit
    @raises:        Exception, if execution time exceeds time limit
    @return:        None
    '''
    # Reading from file and storing each word in a list
    dictionary_file = open(filename, 'r', encoding="utf-8")
    lines = []
    for line in dictionary_file:
        lines.append(line.strip('\n'))
    
    # Starting timer
    start = default_timer()
    taken = default_timer() - start
    # Looping through the word list and loading each word into the hash table
    for key in lines:
        if taken >= time_limit:
            raise Exception("Time limit exceeded")
        hash_table[key] = 1
        taken = default_timer() - start   
        #print(str(taken))

    print("Addition Successful")
    return taken

def load_dictionary_statistics(hash_base, table_size, filename, max_time):
    '''
    This function creates a hash table and loads words from a file to it, returning the number of words entered,
    time, collision count, total probe chain length, max probe chain length and rehash count
    @complexity:    Best Case: O(lines) / Worst Case: O(lines * table_size)
    @input:         hash_base: base value for the hash table
                    table_size: size of hash table
                    filename: Name of file for lines to be added
                    max_time: maximum allowed time limit
    @returns:       tuple
    '''
    # Creating a HashTable object
    hash_table = HashTable(table_size, hash_base)

    # Calling load_dictionary
    try:
        time_taken = load_dictionary(hash_table, filename, max_time)
        collision_count, probe_total, probe_max, rehash_count = hash_table.statistics()
        return hash_table.count, time_taken, collision_count, probe_total, probe_max, rehash_count
    except Exception:
        collision_count, probe_total, probe_max, rehash_count = hash_table.statistics()
        return hash_table.count, None, collision_count, probe_total, probe_max, rehash_count


def table_load_dictionary_statistics(max_time):
    '''
    This function stores the amount of time taken to add words from 
    three text files given different base and table size values, in a csv file
    @complexity:    Best Case: O(num_of_files * num_of_table_sizes * num_of_base_values * num_of_lines_in_txtfile) /
                    Worst Case: O(num_of_files * num_of_table_sizes * num_of_base_values * num_of_lines_in_txtfile * table_size)
    @input:         max_time: maximum allowed time limit
    @returns:       None
    '''
    b = [1, 27183, 250726]
    table_size = [250727, 402221, 1000081]
    filenames = ["english_large.txt", "english_small.txt", "french.txt"]

    with open("output_task4.csv", 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Filename", "Number of Words Added", "Time Taken", "Collisions", "Total Probe", "Max Probe", "Rehashes"])

    for name in filenames:
        for size in table_size:
            for base in b:
                words, time, collisions, probe_length, probe_max, rehashes = load_dictionary_statistics(base, size, name, max_time)
                if time is None:
                    with open("output_task4.csv", 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([name, words, "TIMEOUT", collisions, probe_length, probe_max, rehashes])
                else:
                    with open("output_task4.csv", 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([name, words, round(time, 2), collisions, probe_length, probe_max, rehashes])

#table_load_dictionary_statistics(120)