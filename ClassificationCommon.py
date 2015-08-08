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
