import sys
from ProcessCorpus import *
import Cache

DICTIONARY_PATH = r".\Additional\dictionary.txt"
FACEBOOK_CACHE = r".\Additional\facebook_cache.txt"
DUCKDUCK_WORD_OCCURRENCE_CACHE = r".\Additional\duckduck_word_occurrence_cache.txt"
DUCKDUCK_COMPANY_CACHE = r".\Additional\duckduck_company_cache.txt"


def __main__(argv):

    process_corpus("eng1", 1, argv[0])
    return 1


if __name__ == "__main__":
    __main__(sys.argv[1:])

