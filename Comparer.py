import codecs
from Tokenz import char_encode
import sys


def __main__(argv):
    corpus = ".\Corpus\Entertainment1.txt"
    lang = "en"
    inputf = codecs.open(corpus + "_parsed_result", "r", encoding=char_encode[lang])
    expected = codecs.open(corpus + "_expected", "r", encoding=char_encode[lang])
    outputf = codecs.open(corpus + "_comparison_result", "w", encoding=char_encode[lang])
    tested_lines = inputf.readlines()
    expected_lines = expected.readlines()

    if len(tested_lines) != len(expected_lines):
        raise Exception('bad lines number: expected {} and got {}'.format(len(expected_lines), len(tested_lines)))

    success = partial_success = false_positive = false_negative = confuse = 0
    outputf.writelines("\t".join(["term", "tag_expected", "tag_tested"]) + '\n')

    for line_num in range(len(tested_lines)):

        expected_line = expected_lines[line_num].split(" ")
        tested_line = tested_lines[line_num].split(" ")

        if len(expected_line) != len(tested_line):
            raise Exception('bad line len: expected {} and got {}'.format(len(expected_line), len(tested_line)))

        for i in range(len(expected_line)):
            if expected_line[i] == tested_line[i]:
                success += 1
                continue
            tagged_expected = expected_line[i].split('/')
            tagged_tested = tested_line[i].split('/')
            if tagged_expected[0] != tagged_tested[0]:
                raise Exception(
                    'not the same word: expected {} and got {}'.format(tagged_expected[0], tagged_tested[0]))

            term = tagged_expected[0]
            tag_expected = tagged_expected[1]
            tag_tested = tagged_tested[1]
            outputf.writelines("\t".join([term, tag_expected, tag_tested]) + '\n')

            if tag_expected != 'O' and tag_tested == 'NE':
                partial_success += 1
            else:
                if tag_expected == 'NE' and tag_tested != 'O':  # this should be some other name type
                    confuse += 1
                elif tag_expected != 'O' and tag_expected != 'NE' and tag_tested != 'O' and tag_tested != 'NE':
                    confuse += 1
                elif tag_expected != 'O' and tag_tested == 'O':
                    false_negative += 1
                elif tag_expected == 'O' and tag_tested != 'O':
                    false_positive += 1
                else:  # should not happen
                    raise Exception('Invalid result')
    outputf.writelines(
        'Total Result- success={} partial_success={} confuse={} false_negative={} false_positive={}'.format(
            success, partial_success, confuse, false_negative, false_positive))
    inputf.close()
    outputf.close()


if __name__ == "__main__":
    __main__(sys.argv[1:])
