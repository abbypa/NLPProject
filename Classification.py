from ClassificationCommon import *
from WordOccurrenceClassifier import *
from DuckduckgoSearch import *


class DuckDuckGoWordOccurrenceClassifier:

    def __init__(self):
        self.duckduckgo_search = DuckduckgoSearch(False)
        self.word_occurrence_classifier = WordOccurrenceClassifier(3)

    def classify(self, term):
        search_result = self.duckduckgo_search.general_search(term)
        return self.word_occurrence_classifier.calculate_score(term, search_result)


class UpperCaseClassifier:
    def classify(self, term):
        term_words = term.split()
        if any(word[0].islower() for word in term_words):
            return ClassificationResult(term)
        # else - all words start with a capital letter
        return ClassificationResult(term, {key: 1.0/len(categories) for key in categories})


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


weighted_classifiers = [
    [DuckDuckGoWordOccurrenceClassifier(), 1],
    # [UpperCaseClassifier(), 0.5]
    # [CompanyDuckDuckClassifier(), 1]
]


def classify(term):
    weighted_result = ClassificationResult(term)
    for weighted_classifier in weighted_classifiers:
        result = weighted_classifier[0].classify(term)
        for (key, value) in result.Matches.items():
            weighted_result.Matches[key] += value * weighted_classifier[1]
    return weighted_result
