import re
import sys

category_to_keywords = dict([
    ('person', ['he', 'she', 'born', 'age', 'person', 'people']),
    ('company', ['corp', 'corporation', 'company', 'inc', 'founded']),
    ('place', ['located', 'place', 'city'])
])
categories = category_to_keywords.keys()
delimiters = '[ _(),/.:\n]' #todo- reuse from punctuation list


def calculate_score(term, data):
    classification = Classification_score(term)
    for word in re.split(delimiters, data): #todo- reuse other cleaning code
        if word is '':
            pass
        classification.Total_words += 1
        for key in category_to_keywords:
            if word.lower() in category_to_keywords[key]:
                classification.Matches[key] += 1
    return classification




class Classification_score:
    Term = "",
    Matches = dict()
    Total_words = 0

    def __init__(self, term):
        self.Term = term
        self.Matches = {key: 0 for key in categories}
        self.Total_words = 0