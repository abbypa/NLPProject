from ClassificationCommon import *
from WordOccurrenceClassifier import *
from DuckduckgoSearch import *
from FacebookSearch import *
from DictionarySearch import *
from Cache import *
from Main import DUCKDUCK_WORD_OCCURRENCE_CACHE
from Main import DUCKDUCK_COMPANY_CACHE


class DuckDuckGoWordOccurrenceClassifier:
    def __init__(self):
        self.duckduckgo_search = DuckduckgoSearch(False)
        self.word_occurrence_classifier = WordOccurrenceClassifier()
        self.cache = Cache(DUCKDUCK_WORD_OCCURRENCE_CACHE, "eng1")
        self.cache.load()

    def classify(self, term):
        cache_result = self.cache.search_cache(term)
        if cache_result is not None:
            return ClassificationResult(term, cache_result.Matches)
        search_result = self.duckduckgo_search.general_search(term)
        result = self.word_occurrence_classifier.calculate_score(term, search_result)
        self.cache.update_cache(term, result)
        return result

    def shutdown(self):
        self.cache.save()


class UpperCaseClassifier:
    def __init__(self):
        self.normalized_score = 10

    def classify(self, term):
        term_words = term.split()
        result = ClassificationResult(term)
        if any(word[0].islower() for word in term_words):
            result.Matches['regular'] = self.normalized_score
        else:  # all words start with a capital letter
            result.Matches['person'] = result.Matches['company'] = result.Matches['place'] = self.normalized_score
        return result

    def shutdown(self):
        return 1


class CompanyDuckDuckClassifier:
    def __init__(self):
        self.duckduckgo_search = DuckduckgoSearch(True)
        self.company_postfix = ['corp', 'corporation', 'company', 'inc', 'headquarters']
        self.cache = Cache(DUCKDUCK_COMPANY_CACHE, "eng1")
        self.cache.load()

    def classify(self, term):
        cache_result = self.cache.search_cache(term)
        if self.cache.search_cache(term) is not None:
            return ClassificationResult(term, cache_result.Matches)
        result = ClassificationResult(term)
        for company_word in self.company_postfix:
            term_to_search = term + ' ' + company_word
            if self.duckduckgo_search.general_search(term_to_search) != '':
                result.Matches['company'] += 1
        self.cache.update_cache(term, result)
        return result
    
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
            [DuckDuckGoWordOccurrenceClassifier(), 1],
            # [UpperCaseClassifier(), 1],
            # [CompanyDuckDuckClassifier(), 1],
            # [FacebookClassifier(), 1],
            # [DictionaryClassifier(), 1]
        ]

    def classify(self, term):
        weighted_result = ClassificationResult(term)
        for weighted_classifier in self.weighted_classifiers:
            result = weighted_classifier[0].classify(term)
            for (key, value) in result.Matches.items():
                weighted_result.Matches[key] += value * weighted_classifier[1]
        return weighted_result

    def shutdown(self):
        for classifier in self.weighted_classifiers:
            classifier[0].shutdown()
