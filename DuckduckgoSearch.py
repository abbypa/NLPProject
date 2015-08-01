import duckduckgo
import re

url_regex = 'https://duckduckgo.com(/.+)*/(.+)'
url_compiled_regex = re.compile(url_regex)

def total_search(term):
    return i_feel_lucky(term) + '\n\n' + general_search(term)


def i_feel_lucky(term):
    return duckduckgo.get_zci(term)


def general_search(term):
    r = duckduckgo.query(term)
    all_results = ''

    all_results += try_add_category(r, 'abstract', 'text')
    all_results += try_add_category(r, 'definition', 'text')
    all_results += try_add_category(r, 'answer', 'text')
    all_results += try_add_category(r, 'redirect', 'text')

    all_results += try_add_results(r, "results")
    all_results += try_add_results(r, "related")

    return all_results


def try_add_category(item, category, subcategory):
    try:
        text = getattr(getattr(item, category, None), subcategory, None)
        if text is not None and text != '':
            return category + ': ' + text + '\n'
        return ''
    except: #one category not existing should not fail the others
        pass


def try_add_results(r, category):
    result_str = ''
    results = getattr(r, category, None)
    if results is not None and len(results) > 0:
        result_str += category + ': \n'
        for result in results:
            result_str += try_add_text_and_url(result)
            result_str += try_add_topics(result)
    return result_str


def strip_url(url):
    try:
        stripped_url = url_compiled_regex.match(url).group(2)
    except:
        stripped_url = url
    return stripped_url.replace('?kp=1', '')


def try_add_text_and_url(item):
    try:
        text = item.text
        url = item.url
        if (text is not None and text != '') or (url is not None and url != ''):
            return text + ": " + strip_url(url) + '\n'
    except:
        return ''


def try_add_topics(item):
    result_str = ''
    topics = getattr(item, 'topics', None)
    if topics is not None and len(topics) > 0:
        result_str += 'topics: \n'
        for topic in item.topics:
            try:
                result_str += try_add_text_and_url(topic)
            except:
                pass
    return result_str
