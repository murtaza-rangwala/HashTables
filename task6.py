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
        self.word_frequency = HashTable(size, base)
        self.max = 0
        self.max_key = ""

    def add_file(self, filename):
        file = open(filename, 'r', encoding="utf-8")
        words = []
        for line in file:
            l = line.strip().split()
            for word in l:
                words.append(word)

        self.load_word_frequency_lst(words)

    def load_word_frequency_lst(self, lst):
        
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

        occurences = self.word_frequency[word]

        if word in self.word_frequency:
            if occurences >= (self.max / 100):
                return 0
            elif occurences >= (self.max / 1000) and occurences < (self.max / 100):
                return 1
            else:
                return 2
        else:
            return 3
            
