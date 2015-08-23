import sys
import codecs
from Tokenz import char_encode
from Config import DICTIONARY_PATH, DICTIONARY_NE_GRADE, DICTIONARY_NORMAL_WORD_GRADE, DICTIONARY_ENCODING_LANGUAGE

class DictionarySearch:

    def __init__(self):
        self.dictionary = dict()
        inputf = codecs.open(DICTIONARY_PATH, "r", encoding=char_encode[DICTIONARY_ENCODING_LANGUAGE])
        for w in inputf:
            word = w.split("\r\n")[0].lower()
            self.dictionary[word] = w
        inputf.close()

    def search_dictionary(self,term):
        ne = DICTIONARY_NE_GRADE
        norm = DICTIONARY_NORMAL_WORD_GRADE
        if len(term.split(" "))>1:
            return [0,0,0,0]  #dictionary has single words only, no point checking..
        elif term.isnumeric() or term[0].isdigit():
            return [0,0,0,norm]
        elif term.lower() in self.dictionary.keys():
            if self.dictionary[term.lower()][0].isupper():
                return [ne,ne,ne,0] # might be a NE
            else:
                return [0,0,0,norm] # probably a normal word
        else:
            if term.lower()[-1]=='s': #check for plural word
                if term.lower()[:-1] in self.dictionary.keys():
                    return [0,0,0,norm]
                else:
                    return [ne,ne,ne,0] # probably a NE
            else:
                return [ne,ne,ne,0] # probably a NE
            

