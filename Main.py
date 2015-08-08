import sys
from ProcessCorpus import *

DICTIONARY_PATH = r"C:\Users\Nini\Desktop\limudim\nlproj\git\Additional\dictionary.txt"



def __main__(argv):

    process_corpus("eng1",1,argv[0])

    return 1


if __name__ == "__main__":
    __main__(sys.argv[1:])

