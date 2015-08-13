import sys
from DuckduckgoSearch import *
from WordOccurrenceClassifier import *
from Classification import *


def __main__(argv):

    classifier = Classifier()
    terms = ['Barack Obama', 'Lady Gaga', 'Microsoft', 'Apple', 'San Francisco', 'Grand Canyon', 'Haifa', 'Book', 'Cup', 'Ground', 'Piece', 'Ball', 'Tony']
    #terms = ['United States', 'Michelle Obama', 'paul mccartney', 'Britney Spears', 'White House', 'Tel Aviv', 'Central Park', 'Amazon', 'Costco', 'Sony', 'Samsung', 'dog']
    for term in terms:
        """search_result = general_search(term)
        result = calculate_score(term, search_result)
        print term + ': '
        print result.Matches"""
        print term + ': '
        print classifier.classify(term).Matches



if __name__ == "__main__":
    __main__(sys.argv[1:])
