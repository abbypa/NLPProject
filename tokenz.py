import sys
import re
import codecs

char_encode = {"eng1": "utf-8" , "eng2" : "cp1252"}
punctuation = {",", ":", ";", "\"", r"'", "/", r"\\", "\?", "!", "\(", "\)", "\[", "\]", "\{", "\}", "<" , ">", "-" ,"_"}
punctuation_not_for_regex = {",", ":", ";", "\"", "'", "/", "\\", ".", "?", "!", "(", ")", "[", "]", "{", "}", "<" , ">", "-" ,"_", ".\r\n"}
stop_words = {"s","a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your"}


def split_lines(lang,corpus):
    inputf = codecs.open(corpus, "r", encoding=char_encode[lang])
    outputf = codecs.open(corpus + "_parsed_lines", "w", encoding=char_encode[lang])
    for l in inputf:
        line = l.split(" ")
        line.append(" ")
        cpy = ""
        for i in range(len(line)-1):
            if "." in line[i]:
                if line[i+1][0].islower() or count_dots(line[i])>1:
                    cpy = cpy + " " + line[i]
                else:
                    tmp = line[i].split(".")
                    cpy = cpy + " " + tmp[0] + " .\r\n"
            else:
                cpy = cpy + " " + line[i]
        outputf.write(cpy)
    inputf.close()
    outputf.close()
    return 1

def count_dots(word):
    cnt = 0
    for i in range(len(word)):
        if word[i] == ".":
            cnt+=1
    return cnt


def split_punctuation(lang,corpus):
    inputf = codecs.open(corpus, "r", encoding=char_encode[lang])
    outputf = codecs.open(corpus + "_parsed_punc", "w", encoding=char_encode[lang])
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
            if len(tmp) > 1:
                if tmp[-1] in stop_words:
                    tmp = increase_phrase(i,line,tmp)
            if len(tmp)==0 or tmp[0]=='':
                continue
            else:
               print(i,tmp)
    inputf.close()
                

def increase_phrase(idx, line, seq):
    while True:
        if (idx+len(seq)) >= len(line):
            break
        if line[idx+len(seq)] in punctuation_not_for_regex:
            break
        elif line[idx+len(seq)] in stop_words:
            seq.append(line[idx+len(seq)])
        else:
            seq.append(line[idx+len(seq)])
            break
    return seq
    
def remove_first_sw(seq):
    if len(seq) > 0:
        if seq[0].lower() in stop_words or len(seq[0])==1:
            return ['']
    return seq
    

def strip_punc(seq):
    for idx in range(len(seq)):
        if seq[idx] in punctuation_not_for_regex: #don't search ngram with punctuation in it
            return seq[:idx]
    return seq
    

    
