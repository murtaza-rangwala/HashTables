#!/usr/bin/env python3
"""
:author:    Murtaza Hatim 
:date:      16/10/2019
"""

from HashTable_task6 import HashTable

class Freq:
    '''
    This class performs a frequency analysis on a text file
    '''
    def __init__(self, size = 1103, base = 29):
        '''
        This function initializes all the instance variables of this class
        @complexity:    Best Case: O(1) / Worst Case: O(1)
        @input:         size: size of table
                        base: base value of the hash function
        @return:        None
        '''
        self.word_frequency = HashTable(size, base)
        self.max = 0
        self.max_key = ""

    def add_file(self, filename):
        '''
        This function reads a text file and stores each word from the text file into a hash table 
        @complexity:    O(num_of_lines * num_of_words_in_each_line)
        @input:         filename: name of the text file
        @returns:       None
        '''
        file = open(filename, 'r', encoding="utf-8")
        words = []
        for line in file:
            l = line.strip().split()
            for word in l:
                words.append(word)

        self.load_word_frequency_lst(words)

    def load_word_frequency_lst(self, lst):
        '''
        This function loads loads all words from an array into a hash table while
        recording its occurences at the same time
        @complexity:    Best Case: O(num_of_words) / Worst Case: O(num_of_words * hashtable_size)
        @input:         lst: list of words
        @returns:       None
        '''
        for word in lst:
            data = 1
            if word in self.word_frequency:
                data = self.word_frequency[word] + 1
            self.word_frequency[word] = data

            if self.max < data:
                self.max = data
                self.max_key = word

        print ("Addition Successful")

    def rarity(self, word):
        '''
        This function calculates the rarity score of a word
        in the hash table
        @complexity:    Best Case: O(1) / Worst Case: O(hashtable_size)
        @input:         word: word under consideration
        @returns:       Rarity score (common word = 0, uncommon word = 1, rare word = 2, error = 3)
        '''
        if word in self.word_frequency:
            occurences = self.word_frequency[word]
            if occurences >= (self.max / 100):
                return 0
            elif occurences >= (self.max / 1000) and occurences < (self.max / 100):
                return 1
            else:
                return 2
        else:
            return 3
            


    def evaluate_frequency(self, other_filename):
        '''
        This function evaluate the frequency of each word from other_filename in filename and
        returns percentage of each word type i.e., common, uncommon, rare and errors.
        @complexity:    Best Case: O(num_of_words_in_other_file) / 
                        Worst Case: O(num_of_words_in_other_file * hashtable_size)
        @input:         other_filename: file whos frequency needs to be evaluated
        @returns:       tuple; (percentage of common words, uncommon words, rare words and non existent words respectively)
        '''

        rarity_list = [0] * 4
        
        file = open(other_filename, 'r', encoding="utf-8")
        words = []
        for line in file:
            l = line.strip().split()
            for word in l:
                words.append(word)

        finished_words = HashTable()

        for word in words:

            if not(word in finished_words):
                score = self.rarity(word)
            
                if score == 0:
                    rarity_list[0] += 1
                elif score == 1:
                    rarity_list[1] += 1
                elif score == 2:
                    rarity_list[2] += 1
                else:
                    rarity_list[3] += 1

                finished_words[word] = "Done"

        total = sum(rarity_list)

        common = round((rarity_list[0] / total) * 100, 2)
        uncommon = round((rarity_list[1] / total) * 100, 2)
        rare = round((rarity_list[2] / total) * 100, 2)
        errors = round((rarity_list[3] / total) * 100, 2)

        return (common, uncommon, rare, errors)




            