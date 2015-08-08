import sys
import codecs
from Tokenz import char_encode
from Main import DICTIONARY_PATH

class DictionarySearch:

    def __init__(self):
        self.dictionary = dict()
        inputf = codecs.open(DICTIONARY_PATH, "r", encoding=char_encode["eng2"])
        for w in inputf:
            word = w.split("\n")[0].lower()
            self.dictionary[word] = w
        inputf.close()
        

    def search_dictionary(self,term):
        if len(term.split(" "))>1:
            return [0,0,0,0]  #dictionary has single words only, no point checking..
        if term.lower() in self.dictionary.keys():
            if self.dictionary[term.lower()][0].isupper():
                return [10,10,10,0] # might be a NE
            else:
                return [0,0,0,100] # probably a normal word
        else:
            return [10,10,10,0] # probably a NE
            
