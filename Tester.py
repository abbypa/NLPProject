from DuckduckgoSearch import *
from WordOccurrenceClassifier import *


def __main__(argv):
    terms = ['Barack Obama', 'Lady Gaga', 'Microsoft', 'Apple', 'San Francisco', 'Grand Canyon', 'Book', 'Cup', 'Ground', 'Piece', 'Ball', 'Tony']
    for term in terms:
        search_result = general_search(term)
        result = calculate_score(term, search_result)
        print term + ': '
        print result.Matches


if __name__ == "__main__":
    __main__(sys.argv[1:])