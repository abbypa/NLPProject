from Tokenz import punctuation_for_printing

class OutputFormat:


    def __init__(self,word,tag="regular"):
        self.tag_translation = {"regular" : "O", "person" : "PERSON", "place" : "LOCATION", "company" : "ORGANIZATION" , "ne" : "NE"}
        self.word = word
        self.tag = tag

    def get_output(self):
        if self.word == ".\r\n" or self.word == ".\n":
            return ".\r\n"
        if self.word == "\r\n" or self.word == "\n":
            return "\r\n"
        if self.word.endswith("\n"):
            return self.word.strip() + "/" + self.tag_translation[self.tag] + "\r\n"
        if self.word == " " or self.word == "":
            return ""
        if self.word in punctuation_for_printing:
            return self.word
        return self.word + "/" + self.tag_translation[self.tag] + " "

    def update_tag(self, tag):
        self.tag = tag

    def get_tag(self):
        return self.tag

