import sys
import re
import codecs

char_encode = {"eng1": "utf-8" , "eng2" : "cp1252"}
punctuation = {",", ":", ";", "\"", r"'", "/", r"\\", "\?", "!", "\(", "\)", "\[", "\]", "\{", "\}", "<" , ">", "-" ,"_"}
punctuation_not_for_regex = {",", ":", ";", "\"", "'", "/", "\\", ".", "?", "!", "(", ")", "[", "]", "{", "}", "<" , ">", "-" ,"_", ".\r\n"}


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


    

    
