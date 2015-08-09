from ClassificationCommon import *
from WordOccurrenceClassifier import *
from DuckduckgoSearch import *
from FacebookSearch import *
from DictionarySearch import *


class DuckDuckGoWordOccurrenceClassifier:
    def __init__(self):
        self.duckduckgo_search = DuckduckgoSearch(False)
        self.word_occurrence_classifier = WordOccurrenceClassifier()

    def classify(self, term):
        search_result = self.duckduckgo_search.general_search(term)
        return self.word_occurrence_classifier.calculate_score(term, search_result)


class UpperCaseClassifier:
    def __init__(self):
        self.normalized_score = 10

    def classify(self, term):
        term_words = term.split()
        result = ClassificationResult(term)
        if any(word[0].islower() for word in term_words):
            result.Matches['regular'] = self.normalized_score
        else: # all words start with a capital letter
            result.Matches['person'] = result.Matches['company'] = result.Matches['place'] = self.normalized_score
        return result


class CompanyDuckDuckClassifier:
    def __init__(self):
        self.duckduckgo_search = DuckduckgoSearch(True)
        self.company_postfix = ['corp', 'corporation', 'company', 'inc', 'headquarters']

    def classify(self, term):
        result = ClassificationResult(term)
        for company_word in self.company_postfix:
            term_to_search = term + ' ' + company_word
            if self.duckduckgo_search.general_search(term_to_search) != '':
                result.Matches['company'] += 1
        return result


class FacebookClassifier:
    def __init__(self):
        self.facebook_search = FacebookSearch()

    def classify(self, term):
        cnt = self.facebook_search.search_Facebook(term)
        matches = dict()
        for i in range(len(categories)):
            matches[categories[i]] = cnt[i]
        return ClassificationResult(term, matches)

class DictionaryClassifier:
    def __init__(self):
        self.dictionary_search = DictionarySearch()

    def classify(self, term):
        cnt = self.dictionary_search.search_dictionary(term)
        matches = dict()
        for i in range(len(categories)):
            matches[categories[i]] = cnt[i]
        return ClassificationResult(term, matches)


weighted_classifiers = [
    [DuckDuckGoWordOccurrenceClassifier(), 1],
    # [UpperCaseClassifier(), 1],
    # [CompanyDuckDuckClassifier(), 1],
    # [FacebookClassifier(), 1],
    # [DictionaryClassifier(), 1]
]


def classify(term):
    weighted_result = ClassificationResult(term)
    for weighted_classifier in weighted_classifiers:
        result = weighted_classifier[0].classify(term)
        for (key, value) in result.Matches.items():
            weighted_result.Matches[key] += value * weighted_classifier[1]
    return weighted_result
