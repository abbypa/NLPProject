from Tokenz import char_encode
import codecs
from ClassificationCommon import *
 

class Cache:

    def __init__(self, cache_path,lang):
        self.cache_path = cache_path
        self.lang = lang
        self.cache = dict()

    def load(self):
        try:
            cache_file = codecs.open(self.cache_path, "r", encoding=char_encode[self.lang])
            for l in cache_file:
                tmp = l.split(",")
                matches = dict()
                for i in range(len(categories)):
                    matches[categories[i]] = int(tmp[i+1])
                self.cache[tmp[0]] = ClassificationResult(tmp[0], matches)
            cache_file.close()
        except:  # cache corrupted- continue without
            pass

    def save(self):
        cache_file = codecs.open(self.cache_path, "w", encoding=char_encode[self.lang])
        for term in self.cache.keys():
            tmp = [term]
            tmp.append(self.cache[term].Matches["person"])
            tmp.append(self.cache[term].Matches["company"])
            tmp.append(self.cache[term].Matches["place"])
            tmp.append(self.cache[term].Matches["regular"])
            for i in range(len(tmp)):
                tmp[i] = str(tmp[i])
            cache_file.write(",".join(tmp) + ",\r\n")
        cache_file.close()

    def search_cache(self,term):
        if term in self.cache.keys():
            return self.cache[term]
        else:
            return None

    def update_cache(self,term,classification_result):
        self.cache[term] = classification_result

    def update_cache_from_list(self,term,cnt):
        matches = dict()
        for i in range(len(categories)):
            matches[categories[i]] = cnt[i]
        self.cache[term] = ClassificationResult(term, matches)

        
        
            
