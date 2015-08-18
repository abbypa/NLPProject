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
WORD_OCCURRENCE_MIN_HITS_TO_MATCH = dict([('person', 10), ('company', 15), ('place', 15)])
DICTIONARY_NORMAL_WORD_GRADE = 150
DICTIONARY_NE_GRADE = 10
FACEBOOK_QUERY_LIMIT = 200
FACEBOOK_NE_MIN_COUNT = 25
FACEBOOK_BALANCE_OUT_NAME = 30
FACEBOOK_USER_PRECISE_MUL = 0.1
FACEBOOK_PAGE_PRECISE_MUL = 1
FACEBOOK_PLACE_PRECISE_MUL = 4

# Winner determination-
MAX_GRADE_FOR_REGULAR = 0
WINNER_PERCENT = 0.9

# Classifiers to run-
DUCK_DUCK_GO_WORD_OCCURRENCE_CLASSIFIER_WEIGHT = 1
UPPERCASE_CLASSIFIER_WEIGHT = 0
COMPANY_DUCK_DUCK_GO_CLASSIFIER_WEIGHT = 0
<<<<<<< HEAD
FACEBOOK_CLASSIFIER_WEIGHT = 1
DICTIONARY_CLASSIFIER_WEIGHT = 1
=======
FACEBOOK_CLASSIFIER_WEIGHT = 0
DICTIONARY_CLASSIFIER_WEIGHT = 0
>>>>>>> 888ad406661a6a3db17b6c9493cd592fdb878893
