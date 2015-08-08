from Tokenz import punctuation_not_for_regex

class OutputFormat:


    def __init__(self,word,tag="regular"):
        self.tag_translation = {"regular" : "O", "person" : "PERSON", "place" : "LOCATION", "company" : "ORGANIZATION" , "ne" : "NE"}
        self.word = word
        self.tag = tag

    def get_output(self):
        if self.word == ".\r\n" or self.word == ".\n":
            return ".\r\n"
        if self.word == " " or self.word == "":
            return ""
        if self.word in punctuation_not_for_regex:
            return self.word
        return self.word + "/" + self.tag_translation[self.tag]

    def update_tag(self, tag):
        if self.tag == "regular":
            self.tag = tag
