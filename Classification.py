from ClassificationCommon import *
from WordOccurrenceClassifier import *
from DuckduckgoSearch import *
from FacebookSearch import *
from DictionarySearch import *
from Cache import *
from Config import *


class DuckDuckGoWordOccurrenceClassifier:
    def __init__(self):
        self.duckduckgo_search = DuckduckgoSearch(False)
        self.word_occurrence_classifier = WordOccurrenceClassifier()
        self.cache = Cache(DUCKDUCK_WORD_OCCURRENCE_CACHE, INPUT_LANGUAGE)
        self.cache.load()

    def classify(self, term):
        cache_result = self.cache.search_cache(term)
        if cache_result is not None:
            return self.word_occurrence_classifier.normalize_results(ClassificationResult(term, cache_result.Matches))
        try:
            search_result = self.duckduckgo_search.general_search(term)
        except Exception, e:
            return ClassificationResult(term, {key: -1 for key in categories})

        result = self.word_occurrence_classifier.calculate_score(term, search_result)
        self.cache.update_cache(term, result)
        return self.word_occurrence_classifier.normalize_results(result)

    def shutdown(self):
        self.cache.save()


class UpperCaseClassifier:
    def __init__(self):
        self.normalized_score = UPPERCASE_NORMALIZED_SCORE

    def classify(self, term):
        term_words = term.split()
        result = ClassificationResult(term)
        if any(word[0].islower() and word not in stop_words for word in term_words):
            result.Matches['regular'] = self.normalized_score
        else:  # each word either starts with a capital letter or is a stop words
            result.Matches['person'] = result.Matches['company'] = result.Matches['place'] = self.normalized_score
        return result

    def shutdown(self):
        return 1


class CompanyDuckDuckClassifier:
    def __init__(self):
        self.duckduckgo_search = DuckduckgoSearch(True)
        self.company_postfix = ['corp', 'corporation', 'company', 'inc', 'headquarters']
        self.cache = Cache(DUCKDUCK_COMPANY_CACHE, INPUT_LANGUAGE)
        self.min_hits_to_match = DUCKDUCK_COMPANY_MIN_HITS_TO_MATCH
        self.cache.load()

    def classify(self, term):
        cache_result = self.cache.search_cache(term)
        if self.cache.search_cache(term) is not None:
            return self.normalize_results(ClassificationResult(term, cache_result.Matches))
        result = ClassificationResult(term)
        for company_word in self.company_postfix:
            term_to_search = term + ' ' + company_word
            try:
                if self.duckduckgo_search.general_search(term_to_search) != '':
                    result.Matches['company'] += 1
            except Exception, e:
                return ClassificationResult(term, {key: -1 for key in categories})
        self.cache.update_cache(term, result)
        return self.normalize_results(result)

    def normalize_results(self, classification_result):
        if classification_result.Matches['company'] < self.min_hits_to_match:
            classification_result.Matches['company'] = 0
        return classification_result
    
    def shutdown(self):
        self.cache.save()


class FacebookClassifier:
    def __init__(self):
        self.facebook_search = FacebookSearch()

    def classify(self, term):
        cnt = self.facebook_search.search_Facebook(term)
        matches = dict()
        for i in range(len(categories)):
            matches[categories[i]] = cnt[i]
        return ClassificationResult(term, matches)

    def shutdown(self):
        self.facebook_search.shutdown()


class DictionaryClassifier:
    def __init__(self):
        self.dictionary_search = DictionarySearch()

    def classify(self, term):
        cnt = self.dictionary_search.search_dictionary(term)
        matches = dict()
        for i in range(len(categories)):
            matches[categories[i]] = cnt[i]
        return ClassificationResult(term, matches)

    def shutdown(self):
        return 1


class Classifier:
    def __init__(self):
        self.weighted_classifiers = [
            [DuckDuckGoWordOccurrenceClassifier(), DUCK_DUCK_GO_WORD_OCCURRENCE_CLASSIFIER_WEIGHT],
            [UpperCaseClassifier(), UPPERCASE_CLASSIFIER_WEIGHT],
            [CompanyDuckDuckClassifier(), COMPANY_DUCK_DUCK_GO_CLASSIFIER_WEIGHT],
            [FacebookClassifier(), FACEBOOK_CLASSIFIER_WEIGHT],
            [DictionaryClassifier(), DICTIONARY_CLASSIFIER_WEIGHT]
        ]

    def classify(self, term):
        weighted_result = ClassificationResult(term)
        for weighted_classifier in self.weighted_classifiers:
            if weighted_classifier[1] != 0:
                result = weighted_classifier[0].classify(term)
                for (key, value) in result.Matches.items():
                    weighted_result.Matches[key] += value * weighted_classifier[1]
        return weighted_result

    def shutdown(self):
        for classifier in self.weighted_classifiers:
            classifier[0].shutdown()
