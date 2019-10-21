"""
:author:    Murtaza Hatim 
:date:      17/10/2019
"""

import math
import task1
from timeit import default_timer
import csv
import numpy as np
import matplotlib.pyplot as plt

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


#load_dictionary(task1.HashTable(), "english_small.txt", 10)

def load_dictionary_time(hash_base, table_size, filename, max_time):
    '''
    This function creates a hash table and loads words from a file to it, returning the number of words entered and
    time
    @complexity:    Best Case: O(lines) / Worst Case: O(lines * table_size)
    @input:         hash_base: base value for the hash table
                    table_size: size of hash table
                    filename: Name of file for lines to be added
                    max_time: maximum allowed time limit
    @returns:       tuple; (number of words entered, time taken (if time_taken < max_time, otherwise None))
    '''
    # Creating a HashTable object
    hash_table = task1.HashTable(table_size, hash_base)

    # Calling load_dictionary
    try:
        time_taken = load_dictionary(hash_table, filename, max_time)
        return hash_table.count, time_taken
    except Exception:
        return hash_table.count, None

#print(load_dictionary_time(1, 50000, "english_small.txt", 150))

def table_load_dictionary_time(max_time):
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

    with open("output_task2.csv", 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Filename", "Number of Words Added", "Time Taken"])

    for name in filenames:
        for size in table_size:
            for base in b:
                words, time = load_dictionary_time(base, size, name, max_time)
                if time is None:
                    with open("output_task2.csv", 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([name, words, "TIMEOUT"])
                else:
                    with open("output_task2.csv", 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([name, words, round(time, 2)])


