import duckduckgo
import sys


def i_feel_lucky(term):
    return duckduckgo.get_zci(term)


def add_category_if_exists(item, category, subcategory):
    sub_item = getattr(item, category, None)
    if sub_item is not None:
        text = getattr(sub_item, subcategory, None)
        if text is not None and text != '':
            return category + ': ' + text + '\n'
    return ''


def add_result_if_exists(item, deep=True):
    result_str = ''
    text = getattr(item, 'text', None)
    url = getattr(item, 'url', None)
    if text is not None and url is not None:
        result_str += text + ": " + url
    topics = getattr(item, 'topics', None)
    if topics is not None:
        for topic in topics:
            result_str += add_result_if_exists(topic, False) #no endless recursion!
    return result_str


def general_search(term):
    r = duckduckgo.query(term)
    all_results = ''
    all_results += add_category_if_exists(r, 'abstract', 'text')
    all_results += add_category_if_exists(r, 'definition', 'text')
    all_results += add_category_if_exists(r, 'answer', 'text')
    all_results += add_category_if_exists(r, 'redirect', 'url')

    all_results += 'Results: \n'
    for result in r.results:
        all_results += add_result_if_exists(result)
    all_results += 'Related: \n'
    for related in r.related:
        all_results += add_result_if_exists(related)
    return all_results


def __main__(argv):
    term = 'Eiffel'
    print general_search(term)
    print '\n'
    print i_feel_lucky(term)
    return 1


if __name__ == "__main__":
    __main__(sys.argv[1:])