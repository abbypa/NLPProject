from facepy import GraphAPI

class FacebookSearch:
    company = {"company", "buisness", "computers/technology", "professional services", "product/service"}
    place = {"country", "city", "landmark", "public places", "historical place", "tours/sightseeing", "travel/leisure",
             "national park"}
    person = {"politician", "public figure", "government official", "writer", "athlete", "artist", "musician/band",
              "news personality", "entertainer", "actor/director", "author", "comedian"}

    def __init__(self):
        ##https://developers.facebook.com/tools/explorer/
        user_access_token = "CAACEdEose0cBAOzUbqHZB8aZAY4PqDWHCAjhpqBl2bVn3hliZA12SRk0YHhd3ZBIrU9voOM17SYQaEnBTDdZB4RuVGxxG9oAlIZASKMEaA2pZCZBwIVd47tNxdQkS6PnzRbtcKGAHMzb3EfxkSq2i1hSyhOF3loZBIkMJxKZC19SGNyEZC7NAC7PJdWYWOFLvFxJnAMv2cFtUbVfl1fc7j4IykX"
        self.graph = GraphAPI(user_access_token)

    def search_Facebook(self, term):
        cnt = [0, 0, 0]
        cnt = self.search_name(term, cnt)
        cnt = self.search_company(term, cnt)
        cnt = self.search_place(term, cnt)
        return cnt

    def search_name(self, term, cnt):
        res = self.get_results(term, "user")
        for i in res["data"]:
            # print i
            # if (check_name(i,term)):
            # print graph.get(i["id"] +"?fields=relationship_status")
            cnt[0] += self.check_name(i, term)
        return cnt

    def search_company(self, term, cnt):
        res = self.get_results(term, "page")
        for i in res["data"]:
            # print i
            if i["category"].lower() in self.company:  # use same words as duckduckgo?
                cnt[1] += self.check_name(i, term)
            elif i["category"].lower() in self.person:
                cnt[0] += self.check_name(i, term)
        return cnt

    def search_place(self, term, cnt):
        res = self.get_results(term, "place")
        for i in res["data"]:
            # print i
            if i["category"].lower() in self.place:  # use same words as duckduckgo?
                cnt[2] += self.check_name(i, term)
            for idx in range(len(i["category_list"])):
                if i["category_list"][idx]["name"].lower() in self.place:
                    cnt[2] += self.check_name(i, term)
        return cnt

    @staticmethod
    def check_name(res, term):
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
