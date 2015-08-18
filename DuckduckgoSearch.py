import duckduckgo
import re
import time
from Config import INPUT_LANGUAGE


class DuckduckgoSearch:
    def __init__(self, verbosity=False):
        self.url_regex = 'https://duckduckgo.com(/.+)*/(.+)'
        self.url_compiled_regex = re.compile(self.url_regex)
        self.verbosity = verbosity
        self.language = INPUT_LANGUAGE.lower() + '_' + INPUT_LANGUAGE.upper()

    def total_search(self, term):
        return self.i_feel_lucky(term) + '\n\n' + self.general_search(term)

    def i_feel_lucky(self, term):
        return duckduckgo.get_zci(term, kad=self.language)

    def general_search(self, term):
        try:
            r = duckduckgo.query(term, kad=self.language)
        except:
            print "duckduck search error, trying again in 30 seconds..."
            time.sleep(30)
            r = duckduckgo.query(term, kad=self.language)
        all_results = ''
        all_results += self.try_add_category(r, 'abstract', 'text')
        all_results += self.try_add_category(r, 'definition', 'text')
        all_results += self.try_add_category(r, 'answer', 'text')
        all_results += self.try_add_category(r, 'redirect', 'text')
        all_results += self.try_add_results(r, "results")
        all_results += self.try_add_results(r, "related")
        return all_results

    def try_add_category(self, item, category, subcategory):
        try:
            text = getattr(getattr(item, category, None), subcategory, None)
            if text is not None and text != '':
                if self.verbosity:
                    return category + ': ' + text + '\n'
                return text + '\n'
            return ''
        except:  # one category not existing should not fail the others
            pass

    def try_add_results(self, r, category):
        result_str = ''
        results = getattr(r, category, None)
        if results is not None and len(results) > 0:
            if self.verbosity:
                result_str += category + ': \n'
            for result in results:
                result_str += self.try_add_text_and_url(result)
                result_str += self.try_add_topics(result)
        return result_str

    def strip_url(self, url):
        try:
            stripped_url = self.url_compiled_regex.match(url).group(2)
        except:
            stripped_url = url
        stripped_url = stripped_url.replace('&kad=' + self.language, '')
        return stripped_url.replace('?kp=1', '')

    def try_add_text_and_url(self, item):
        try:
            text = item.text
            url = item.url
            if (text is not None and text != '') and (url is not None and url != ''):
                return text + ": " + self.strip_url(url) + '\n'
            return ''
        except:
            return ''

    def try_add_topics(self, item):
        result_str = ''
        topics = getattr(item, 'topics', None)
        if topics is not None and len(topics) > 0:
            if self.verbosity:
                result_str += 'topics: \n'
            for topic in item.topics:
                try:
                    result_str += self.try_add_text_and_url(topic)
                except:
                    pass
        return result_str
