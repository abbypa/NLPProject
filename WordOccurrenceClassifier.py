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
        return ClassificationResult(term, hits)

    def normalize_results(self, classification_result):
        for category in categories:
            if category != 'regular' and classification_result.Matches[category] < self.min_hits_to_match:
                classification_result.Matches[category] = 0
        if sum(classification_result.Matches.values()) == 0:
            classification_result.Matches['regular'] = self.min_hits_to_match
        return classification_result
