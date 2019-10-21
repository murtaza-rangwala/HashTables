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

        rarity_list = [0] * 4
        
        file = open(other_filename, 'r', encoding="utf-8")
        words = []
        for line in file:
            l = line.strip().split()
            for word in l:
                words.append(word)

        for word in words:
            score = self.rarity(word)
            
            if score == 0:
                rarity_list[0] += 1
            elif score == 1:
                rarity_list[1] += 1
            elif score == 2:
                rarity_list[2] += 1
            else:
                rarity_list[3] += 1

        total = sum(rarity_list)

        common = round((rarity_list[0] / total) * 100, 2)
        uncommon = round((rarity_list[1] / total) * 100, 2)
        rare = round((rarity_list[2] / total) * 100, 2)
        errors = round((rarity_list[3] / total) * 100, 2)

        return (common, uncommon, rare, errors)




            