### FIX - U.S


import sys
import re
import codecs

char_encode = {"eng1": "utf-8" , "eng2" : "cp1252"}
punctuation = {",", ":", ";", "\"", r"'", "/", r"\\", "\.", "\?", "!", "\(", "\)", "\[", "\]", "\{", "\}", "<" , ">", "-" ,"_"}
punctuation_not_for_regex = {",", ":", ";", "\"", "'", "/", "\\", ".", "?", "!", "(", ")", "[", "]", "{", "}", "<" , ">", "-" ,"_"}
stop_words = {"s","a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your"}


def split_lines(lang,corpus):
    return 1


def split_punctuation(lang,corpus):
    inputf = codecs.open(corpus, "r", encoding=char_encode[lang])
    outputf = codecs.open(corpus + "_parsed", "w", encoding=char_encode[lang])
    for line in inputf:
        for sym in punctuation: #pad punctuation marks with space
            if len(sym)==1:
                line = re.sub(sym, " " + sym + " ", line)
            else:
                line = re.sub(sym, " " + sym[1] + " ", line)
        line = re.sub("  ", " ",line)
        outputf.write(line)
    inputf.close()
    outputf.close()
    return 1


def process_corpus(lang, ngram, corpus):
    inputf = codecs.open(corpus, "r", encoding=char_encode[lang])
    for l in inputf:
        line = l.split(" ")
        for i in range(len(line)-ngram):
            tmp = line[i:i+ngram]
            tmp = strip_punc(tmp)
            tmp = remove_first_sw(tmp)
            #if len(tmp) > 1:
                #consider increasing window
            if len(tmp)==0 or tmp[0]=='':
                continue
            else:
               print(i,tmp)
    inputf.close()
                
    
def remove_first_sw(seq):
    if len(seq) > 0:
        if seq[0].lower() in stop_words:
            return ['']
    return seq
    

def strip_punc(seq):
    for idx in range(len(seq)):
        if seq[idx] in punctuation_not_for_regex: #don't search ngram with punctuation in it
            seq = seq[:idx]
            break
    return seq
    

    
