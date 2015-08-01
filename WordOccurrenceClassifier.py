import re
from ClassificationCommon import *


class WordOccurrenceClassifier:

    def __init__(self, min_hits_to_match=3):
        self.category_to_keywords = dict([
            ('person', ['he', 'she', 'born', 'age', 'person', 'people', 'his', 'her']),
            ('company', ['corp', 'corporation', 'company', 'companies', 'inc',
                         'founded', 'headquarters', 'headquartered']),
            ('place', ['located', 'place', 'places', 'city', 'cities', 'country',
                       'countries', 'area', 'areas', 'region', 'regions'])
        ])
        self.categories = self.category_to_keywords.keys()
        self.delimiters = '[ _(),/.:\n]'     # todo- reuse from punctuation list
        self.min_hits_to_match = min_hits_to_match

    def calculate_score(self, term, data):
        hits = {key: 0 for key in categories}
        for word in re.split(self.delimiters, data):     # todo- reuse other cleaning code
            if word is '':
                pass
            for key in self.category_to_keywords:
                if word.lower() in self.category_to_keywords[key]:
                    hits[key] += 1
        return ClassificationResult(term, self.normalize_results(hits))

    def normalize_results(self, hits):
        '''for key in hits.keys():
            if hits[key] < MIN_HITS_TO_MATCH: #todo- param to class
                hits[key] = 0
        normalization_factor = float(sum(hits.values()))  # todo- consider using the total amount of words instead
        if normalization_factor != 0:
            return {key: value / normalization_factor for (key, value) in hits.items()}'''
        return hits
