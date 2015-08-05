from facepy import GraphAPI

##https://developers.facebook.com/tools/explorer/
company = {"company", "buisness", "computers/technology", "professional services", "product/service"}
place = {"country", "city", "landmark", "public places", "historical place", "tours/sightseeing", "travel/leisure", "national park"}
person = {"politician", "public figure", "government official", "writer", "athlete", "artist", "musician/band", "news personality", "entertainer", "actor/director", "author", "comedian"}


user_access_token = "CAACEdEose0cBAAZCJOL2ONbKhtHxyunm8ZAFdghVXypifxZBqNYJdo5f4eR0ZBBQvlAZBLw6wGHJQjsXehbkH0YCKYVyU24ApXzX3U40ARf7OqZBZAcEPrC5spfZB5ucQ4NZCrpWvsZBnLGZAAZBhpyUH23VomuE4zG76dN9ZCnFPZAfhtdHykcg9ZAlwEA2xhFw6za9sVA5PHqWoayZCJPyLlH8aeEq"
graph = GraphAPI(user_access_token)


def searchFacebook(term):
    cnt = [0,0,0]
    cnt = searchname(term,cnt)
    cnt = searchcompany(term,cnt)
    cnt = searchplace(term,cnt)
    print(cnt)


def searchname(term,cnt):
    res = getresults(term,"user")
    for i in res["data"]:
        print i
        #if (checkname(i,term)):
            #print graph.get(i["id"] +"?fields=relationship_status")
        cnt[0]+=checkname(i,term)
    return cnt


def searchcompany(term,cnt):
    res = getresults(term,"page")
    for i in res["data"]:
        #print i
        if i["category"].lower() in company: #use same words as duckduckgo?
            cnt[1]+=checkname(i,term)
        elif i["category"].lower() in person:
            cnt[0]+=checkname(i,term)
    return cnt

def searchplace(term,cnt):
    res = getresults(term,"place")
    for i in res["data"]:
        #print i
        if i["category"].lower() in place: #use same words as duckduckgo?
            cnt[2] += checkname(i,term)
        for idx in range(len(i["category_list"])):
            if i["category_list"][idx]["name"].lower() in place:
                cnt[2] += checkname(i,term)
    return cnt

def checkname(res,term):
    if len(term.split(" ")) == 1:
        tmp = res["name"].split(" ")
        for x in tmp:
            if x.lower()==term.lower():
                return 1
    else:
        if term.lower() in res["name"].lower():
            return 1
    return 0
    
def getresults(term, querytype):
    return graph.search(term,querytype,limit=200)
