#!/usr/bin/env python3
"""
:author:    Murtaza Hatim 
:date:      20/10/2019
"""

from BinarySearchTree import BinarySearchTree
from timeit import default_timer
import math
import csv

class HashTable:

  def __init__(self, table_capacity = 1103, hash_base = 29):
    self.table = [None] * table_capacity
    self.table_size = table_capacity
    self.count = 0
    self.base = hash_base
    self.count = 0
    self.collision_count = 0
    self.probe_total = 0
    self.probe_max = 0
    self.rehash_count = 0

  def hash_function(self, key):
    value = 0
    for i in range(len(key)):
      value = ((value * self.base) + ord(key[i])) % self.table_size
    return value

  def __setitem__(self, key, data):
    pos = self.hash_function(key)

    if self.table[pos] is None:
        my_tree = BinarySearchTree()
        my_tree[key] = data
        self.table[pos] = my_tree
        self.count += 1
        return
    else:
        flag = False
        if not(key in self.table[pos]):
            flag = True

        self.table[pos][key] = data;

        if flag:
            probe = self.table[pos].count 
            self.probe_total += self.table[pos].count 
            self.collision_count += 1
            self.count += 1

            if self.probe_max < self.table[pos].count:
                self.probe_max = self.table[pos].count

        return
    
  def __getitem__(self, key):
    pos = self.hash_function(key)

    if self.table[pos] is None:
      raise KeyError("key not found")
      return
    else:
      return self.table[pos][key]

  def __contains__(self, key):
      '''
      This function returns if key exists in table or not
      @complexity:    Best Case: O(1) / Worst Case: O(table_size)
      @input:         key: key from the key value pairs stored in the Hash Table
      @returns:       True if key exists in Hash table, False otherwise
      '''
      pos = self.hash_function(key)
      
      if self.table[pos] is None:
          return False
      else:
          if key in self.table[pos]:
              return True
          else:
              return False
    
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
    dictionary_file = open(filename, 'r')
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

    with open("output_task5.csv", 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Filename", "Number of Words Added", "Time Taken", "Collisions", "Total Probe", "Max Probe", "Rehashes"])

    for name in filenames:
        for size in table_size:
            for base in b:
                words, time, collisions, probe_length, probe_max, rehashes = load_dictionary_statistics(base, size, name, max_time)
                if time is None:
                    with open("output_task5.csv", 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([name, words, "TIMEOUT", collisions, probe_length, probe_max, rehashes])
                else:
                    with open("output_task5.csv", 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([name, words, round(time, 2), collisions, probe_length, probe_max, rehashes])

table_load_dictionary_statistics(120)