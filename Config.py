# Al configurable parameters

# General
NGRAM = 1

# Language
DICTIONARY_ENCODING_LANGUAGE = 'eng2'
INPUT_LANGUAGE = 'en'

# Paths-
DICTIONARY_PATH = r".\Additional\dictionary.txt"
FACEBOOK_CACHE = r".\Additional\facebook_cache.txt"
DUCKDUCK_WORD_OCCURRENCE_CACHE = r".\Additional\duckduck_word_occurrence_cache.txt"
DUCKDUCK_COMPANY_CACHE = r".\Additional\duckduck_company_cache.txt"

# Specific classifiers numeric configurations-
UPPERCASE_NORMALIZED_SCORE = 10
WORD_OCCURRENCE_MIN_HITS_TO_MATCH = 9
DICTIONARY_NORMAL_WORD_GRADE = 150
DICTIONARY_NE_GRADE = 10

# Winner determination-
MAX_GRADE_FOR_REGULAR = 0
WINNER_PERCENT = 0.9

# Classifiers to run-
DUCK_DUCK_GO_WORD_OCCURRENCE_CLASSIFIER_WEIGHT = 0
UPPERCASE_CLASSIFIER_WEIGHT = 0
COMPANY_DUCK_DUCK_GO_CLASSIFIER_WEIGHT = 0
FACEBOOK_CLASSIFIER_WEIGHT = 0
DICTIONARY_CLASSIFIER_WEIGHT = 1
