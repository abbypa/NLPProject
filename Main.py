import sys
import os
from ProcessCorpus import *
from Tokenz import *


def __main__(argv):
    if len(argv)!=1:
        print " Usage: Main.py <corpus>"
        return 1
    reload(sys)
    sys.setdefaultencoding('utf-8')
    split_lines("eng1",argv[0])
    split_punctuation("eng1",argv[0] + "_p")
    os.remove(argv[0] + "_p")
    process_corpus("eng1", 1, argv[0] + "_parsed")
    return 1


if __name__ == "__main__":
    __main__(sys.argv[1:])

