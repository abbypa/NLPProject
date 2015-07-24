import re
from ClassificationCommon import *

category_to_keywords = dict([
    ('person', ['he', 'she', 'born', 'age', 'person', 'people']),
    ('company', ['corp', 'corporation', 'company', 'inc', 'founded']),
    ('place', ['located', 'place', 'city'])
])
categories = category_to_keywords.keys()
delimiters = '[ _(),/.:\n]'     # todo- reuse from punctuation list
MIN_HITS_TO_MATCH = 3


def calculate_score(term, data):
    hits = {key: 0 for key in categories}
    total_words = 0
    for word in re.split(delimiters, data):     # todo- reuse other cleaning code
        if word is '':
            pass
        for key in category_to_keywords:
            if word.lower() in category_to_keywords[key]:
                hits[key] += 1
    return ClassificationResult(term, normalize_results(hits))


def normalize_results(hits):
    for key in hits.keys():
        if hits[key] < MIN_HITS_TO_MATCH: #todo- param to class
            hits[key] = 0
    normalization_factor = float(sum(hits.values()))  # todo- consider using the total amount of words instead
    if normalization_factor != 0:
        return {key: value / normalization_factor for (key, value) in hits.items()}
    return hits

