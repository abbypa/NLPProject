from facepy import GraphAPI

class FacebookSearch:
    company = {"company", "buisness", "computers/technology", "professional services", "product/service"}
    place = {"country", "city", "landmark", "public places", "historical place", "tours/sightseeing", "travel/leisure",
             "national park"}
    person = {"politician", "public figure", "government official", "writer", "athlete", "artist", "musician/band",
              "news personality", "entertainer", "actor/director", "author", "comedian"}

    def __init__(self):
        ##https://developers.facebook.com/tools/explorer/
        user_access_token = "CAACEdEose0cBAKuDtgOAeIjs5meUktdZAyvKq1JO89Od5ad2hU0ibZBIscDGQGZAcksIJuKDswwK8OY9suXj3HuSYZBc02cfRZAZCZBoFwNiiIZAzhixZCTh0S753r8qh9yx2hm2g2BVbEFt9LkoVnl3vwkktgFNEGueFtZA1CKDR76mqZAVk8ll8Vqiz5eEN0lpvZALsgVgpVFEMdeZA3akSozVX"
        self.graph = GraphAPI(user_access_token)

    def search_Facebook(self, term):
        cnt = [0, 0, 0, 0]
        cnt = self.search_user(term, cnt)
        cnt = self.search_page(term, cnt)
        cnt = self.search_place(term, cnt)
        if sum(cnt) < 15:
            cnt = [0, 0, 0, 10]
        return cnt

    def search_user(self, term, cnt):
        res = self.get_results(term, "user")
        for i in res["data"]:
            #print i
            #if (self.check_name(i,term,1)):
            #    print self.graph.get(i["id"])
            cnt[0] += self.check_name(i, term, 0.1)
        return cnt

    def search_page(self, term, cnt):
        res = self.get_results(term, "page")
        for i in res["data"]:
            #print i
            if i["category"].lower() in self.company:
                cnt[1] += self.check_name(i, term, 1)
            elif i["category"].lower() in self.person:
                cnt[0] += self.check_name(i, term, 1)
        return cnt

    def search_place(self, term, cnt):
        res = self.get_results(term, "place")
        for i in res["data"]:
            # print i
            if i["category"].lower() in self.place:  
                cnt[2] += self.check_name(i, term, 2)
            for idx in range(len(i["category_list"])):
                if i["category_list"][idx]["name"].lower() in self.place:
                    cnt[2] += self.check_name(i, term, 2)
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
