import sys
from ProcessCorpus import *
import Cache

DICTIONARY_PATH = r".\Additional\dictionary.txt"
FACEBOOK_CACHE = r".\Additional\facebook_cache.txt"


def __main__(argv):

    process_corpus("eng1", 1, argv[0])
    return 1


if __name__ == "__main__":
    __main__(sys.argv[1:])

