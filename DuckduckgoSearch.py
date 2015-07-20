import duckduckgo
import sys


def i_feel_lucky(term):
    return duckduckgo.get_zci(term)


def category_if_not_empty(category, text):
    if text != '':
        return category + ': ' + text + '\n'
    return ''


def general_search(term):
    r = duckduckgo.query(term)
    all_results = ''
    all_results += category_if_not_empty('Abstract', r.abstract.text)
    all_results += category_if_not_empty('Definition', r.definition.text)
    all_results += category_if_not_empty('Answer', r.answer.text)
    all_results += category_if_not_empty('Redirect', r.redirect.url)
    for result in r.results:
        all_results += category_if_not_empty(result.text, result.url)
    all_results += 'Related: '
    for related in r.related:
        all_results += related.text + ','
    return all_results


def __main__(argv):
    term = 'Golden Gate Bridge'
    print general_search(term)
    print '\n'
    print i_feel_lucky(term)
    return 1


if __name__ == "__main__":
    __main__(sys.argv[1:])