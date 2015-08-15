# -*- coding: utf-8 -*-

categories = ['person', 'company', 'place', 'regular']


class ClassificationResult:
    Term = "",
    Matches = dict()

    def __init__(self, term, matches=None):
        self.Term = term
        if matches is None:
            self.Matches = {key: 0 for key in categories}
        else:
            self.Matches = matches


stop_words = {u'’',"-","t","d","ll","ve","m","re","s", "a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any",
              "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do",
              "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her",
              "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least",
              "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of",
              "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she",
              "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they",
              "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which",
              "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your"}
