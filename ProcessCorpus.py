from Tokenz import char_encode, punctuation_not_for_regex
import codecs
from Classification import *
from OutputFormat import *
import time

stop_words = {"s", "a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any",
              "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do",
              "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her",
              "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least",
              "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of",
              "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she",
              "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they",
              "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which",
              "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your"}


def process_corpus(lang, ngram, corpus):
    classifier = Classifier()
    inputf = codecs.open(corpus, "r", encoding=char_encode[lang])
    outputf = codecs.open(corpus + "_result", "w", encoding=char_encode[lang])
    for l in inputf:
        time.sleep(1)
        line = l.split(" ")
        result = copy_line(line)
        for i in range(len(line) - ngram):
            if result[i].get_tag() == "regular":
                term = line[i:i + ngram]
                term = fix_term(line, i, term)
                if len(term) != 0 and term[0] != '':
                    result = test_term(result, line, i, term, "backward", classifier)
        print_result(outputf, result)
    inputf.close()
    outputf.close()
    classifier.shutdown()


def get_winner(grades):
    maxval = max(grades.values())
    if maxval > 0:
        if grades.values().count(maxval) == 1:
            for x in grades.keys():
                if grades[x] == maxval:
                    return x
        else:
            return "ne"
    else:
        return "regular"


def test_term(output, line, index, term, direction, classifier):
    # print term
    grades = classifier.classify(" ".join(term)).Matches
    new_tag = get_winner(grades)
    if new_tag != "regular":
        update_output(output, index, term, new_tag)
        test_larger_window(output, line, index, term, direction, classifier)
    return output


def fix_term(line, index, term):
    term = strip_punc(term)
    term = remove_first_sw(term)
    if len(term) > 1:
        if term[-1] in stop_words:
            term = increase_phrase(index, line, term)
    return term


def test_larger_window(output, line, index, term, direction, classifier):
    if direction != "forward":
        if (index - 1) >= 0 and line[index - 1] not in punctuation_not_for_regex and line[index - 1] not in stop_words:
            new_term = line[index - 1:index + len(term)]
            return test_term(output, line, index - 1, new_term, "backward", classifier)
        return test_larger_window(output, line, index, term, "forward", classifier)
    else:
        if (index + len(term) + 1) < len(line):
            new_term = line[index:index + len(term) + 1]
            new_term = fix_term(line, index, new_term)
            if new_term == term:
                return output
            return test_term(output, line, index, new_term, "forward", classifier)
    return output


def print_result(outputfile, result):
    for i in range(len(result)):
        outputfile.write(result[i].get_output() + " ")


def update_output(output, index, term, tag):
    for x in range(len(term)):
        output[index + x].update_tag(tag)
    return output


def copy_line(line):
    res = []
    for i in range(len(line)):
        res.append(OutputFormat(line[i]))
    return res


def increase_phrase(idx, line, seq):
    while True:
        if (idx + len(seq)) >= len(line):
            break
        if line[idx + len(seq)] in punctuation_not_for_regex:
            break
        elif line[idx + len(seq)] in stop_words:
            seq.append(line[idx + len(seq)])
        else:
            seq.append(line[idx + len(seq)])
            break
    return seq


def remove_first_sw(seq):
    if len(seq) > 0:
        if seq[0].lower() in stop_words or len(seq[0]) == 1:
            return ['']
    return seq


def strip_punc(seq):
    for idx in range(len(seq)):
        if seq[idx] in punctuation_not_for_regex:  # don't search ngram with punctuation in it
            return seq[:idx]
    return seq
