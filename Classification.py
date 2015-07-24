from ClassificationCommon import *
from WordOccurrenceClassifier import *
from DuckduckgoSearch import *


class DuckDuckGoWordOccurrenceClassifier:
    def classify(self, term):
        return calculate_score(term, general_search(term))


class UpperCaseClassifier:
    def classify(self, term):
        term_words = term.split()
        if any(word[0].islower() for word in term_words):
            return ClassificationResult(term)
        # else - all words start with a capital letter
        return ClassificationResult(term, {key: 1.0/len(categories) for key in categories})


weighted_classifiers = [
    [DuckDuckGoWordOccurrenceClassifier(), 0.5],
    [UpperCaseClassifier(), 0.5]
]


def classify(term):
    weighted_result = ClassificationResult(term)
    for weighted_classifier in weighted_classifiers:
        result = weighted_classifier[0].classify(term)
        for (key, value) in result.Matches.items():
            weighted_result.Matches[key] += value * weighted_classifier[1]
    return weighted_result
