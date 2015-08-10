import sys
from ProcessCorpus import *
import Cache

DICTIONARY_PATH = r"C:\Users\Nini\Desktop\limudim\nlproj\git\Additional\dictionary.txt"
FACEBOOK_CACHE = r"C:\Users\Nini\Desktop\limudim\nlproj\git\Additional\facebook_cache.txt"


def __main__(argv):
    
    process_corpus("eng1",1,argv[0])

    for classifier in weighted_classifiers:
        classifier[0].shutdown()
    return 1


if __name__ == "__main__":
    __main__(sys.argv[1:])

