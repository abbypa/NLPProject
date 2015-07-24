class ClassificationResult:
    Term = "",
    Matches = dict()

    def __init__(self, term):
        self.Term = term
        self.Matches = {key: 0 for key in categories}

    def __init__(self, term, matches):
        self.Term = term
        self.Matches = matches

categories = ['person', 'company', 'place']
