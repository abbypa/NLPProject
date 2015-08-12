from facepy import GraphAPI
from Cache import *
from Main import FACEBOOK_CACHE
import random
import time

class FacebookSearch:
    company = {"company", "non-profit organization","organization", "professional services", "product/service", "government organization", "church/religious organization"}
    place = {"country", "city", "landmark", "public places", "historical place", "tours/sightseeing", "travel/leisure",
             "national park", "neighborhood"}
    person = {"politician", "public figure", "government official", "writer", "athlete", "artist", "musician/band",
              "news personality", "entertainer", "actor/director", "author", "comedian"}

    def __init__(self):
        ##https://developers.facebook.com/tools/explorer/
        user_access_token = "CAACEdEose0cBAEcd2mMYlweAFA6TZCXZCEcNB3XbSHk59LglGFq0sAPZBiRi1PjWidCZCCRYStKnNLEoMB5dZAG4ENI4d3R8aJFrZB2sPMKTzliwvxCluHzhnaWwce1tEXsiuMZAExlYaNdR8pkCX0EaLvguzS7EAfaO0ISv7obbp8GHqxAlzncihPk9Kag6zpq3ZCm6OTSqL1hZAEwBjfcZCZA"
        self.graph = GraphAPI(user_access_token)
        self.fb_cache = Cache(FACEBOOK_CACHE,"eng1")
        self.fb_cache.load()
        self.sleep_count = 0

    def shutdown(self):
        self.fb_cache.save()

    def search_Facebook(self, term):
        cache_result = self.fb_cache.search_cache(term)
        if cache_result is None:
            self.sleep_count +=1
            if self.sleep_count == 5:
                time.sleep(random.randint(1,5))
                self.sleep_count = 0
            cnt = [0, 0, 0, 0]
            cnt = self.search_user(term, cnt)
            cnt = self.search_page(term, cnt)
            cnt = self.search_place(term, cnt)
            self.fb_cache.update_cache_from_list(term,cnt)
        else:
            m = cache_result.Matches
            cnt = [m["person"],m["company"],m["place"],m["regular"]]
            for i in range(len(cnt)):
                cnt[i] = float(cnt[i])
        if sum(cnt) < 25:
            cnt = [0, 0, 0, 10]
        if cnt[1] + cnt[2] > 30:
            cnt[0] = cnt[0]/10
        return cnt

    def search_user(self, term, cnt):
        res = self.get_results(term, "user")
        for i in res["data"]:
            #print i
            cnt[0] += self.check_name(i, term, 0.1)
        return cnt

    def search_page(self, term, cnt):
        res = self.get_results(term, "page")
        for i in res["data"]:
            #print i
            if i["category"].lower() in self.person:
                cnt[0] += self.check_name(i, term, 1)
            elif i["category"].lower() in self.company:
                cnt[1] += self.check_name(i, term, 1)
        return cnt

    def search_place(self, term, cnt):
        res = self.get_results(term, "place")
        for i in res["data"]:
            #print i
            if i["category"].lower() in self.place:  
                cnt[2] += self.check_name(i, term, 4)
            for idx in range(len(i["category_list"])):
                if i["category_list"][idx]["name"].lower() in self.place:
                    cnt[2] += self.check_name(i, term, 4)
        return cnt

    @staticmethod
    def check_name(res, term, mul):
        if term.lower()== res["name"].lower():
            return 10 * mul
        if len(term.split(" ")) == 1:
            tmp = res["name"].split(" ")
            for x in tmp:
                if x.lower() == term.lower():
                    return 1
        else:
            if term.lower() in res["name"].lower():
                return 1
        return 0

    def get_results(self, term, querytype):
        return self.graph.search(term, querytype, limit=200)
