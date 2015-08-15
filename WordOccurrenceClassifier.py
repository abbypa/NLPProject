import re
from ClassificationCommon import *
from Config import WORD_OCCURRENCE_MIN_HITS_TO_MATCH

class WordOccurrenceClassifier:

    def __init__(self):
        self.category_to_keywords = dict([
            ('person', ['he', 'she', 'born', 'age', 'person', 'people', 'his', 'her', 'raised',
                        'man', 'men', 'woman', 'women', 'male', 'female',
                        'politician', 'artist', 'writer', 'athlete', 'musician', 'entertainer',
                        'actor', 'director', 'author', 'comedian',
                        'husband', 'wife', 'son', 'daughter', 'brother', 'sister']),
            ('company', ['corp', 'corporation', 'company', 'companies', 'inc', 'conglomerate',
                         'founded', 'headquarters', 'headquartered', 'business', 'product', 'products']),
            ('place', ['located', 'place', 'places', 'city', 'cities', 'country', 'countries',
                       'area', 'areas', 'region', 'regions', 'landmark', 'landmarks', 'travel', 'park', 'parks',
                       'population', 'populated', 'district', 'districts'])
        ])
        self.categories = self.category_to_keywords.keys()
        self.delimiters = '[ _(),/.:\n]'
        self.min_hits_to_match = WORD_OCCURRENCE_MIN_HITS_TO_MATCH

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
