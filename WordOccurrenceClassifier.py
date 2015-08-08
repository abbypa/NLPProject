import re
from ClassificationCommon import *


class WordOccurrenceClassifier:

    def __init__(self):
        self.category_to_keywords = dict([
            ('person', ['he', 'she', 'born', 'age', 'person', 'people', 'his', 'her',
                        'politician', 'artist', 'writer', 'athlete', 'musician', 'entertainer',
                        'actor', 'director', 'author', 'comedian',
                        'husband', 'wife', 'son', 'daughter', 'brother', 'sister']),
            ('company', ['corp', 'corporation', 'company', 'companies', 'inc',
                         'founded', 'headquarters', 'headquartered', 'business', 'product', 'products']),
            ('place', ['located', 'place', 'places', 'city', 'cities', 'country', 'countries',
                       'area', 'areas', 'region', 'regions', 'landmark', 'landmarks', 'travel', 'park', 'parks'])
        ])
        self.categories = self.category_to_keywords.keys()
        self.delimiters = '[ _(),/.:\n]'
        self.min_hits_to_match = 5

    def calculate_score(self, term, data):
        hits = {key: 0 for key in categories}
        for word in re.split(self.delimiters, data):
            if word is '':
                pass
            for key in self.category_to_keywords:
                if word.lower() in self.category_to_keywords[key]:
                    hits[key] += 1
        return ClassificationResult(term, self.normalize_results(hits))

    def normalize_results(self, hits):
        for category in categories:
            if category != 'regular' and hits[category] < self.min_hits_to_match:
                hits[category] = 0
        if sum(hits.values()) == 0:
            hits['regular'] = self.min_hits_to_match
        return hits
