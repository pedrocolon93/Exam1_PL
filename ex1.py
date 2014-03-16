__author__ = 'Pedro'
import re

class Trio:
    def __init__(self, word, linenum):
        self.word = word
        self.amount = 1
        self.lines = []
        self.lines.append(linenum)
    def add_line_number(self, linenum):
        self.lines.append(linenum)
        self.amount = self.amount+1
    def get_word(self):
        return self.word
    def get_lines(self):
        return self.lines
    def get_amount(self):
        return self.amount


def main(filelocation):
    words = []
    file = open(filelocation, 'r')
    pattern = re.compile('\\S+')
    linno = 1
    for line in file:
        print "Currentline:",line
        listofwords = pattern.findall(line)
        print "List of matches",listofwords
        for word in listofwords:
            found = False
            for item in words:
                if item.get_word().lower() == word:
                    found = True
                    item.add_line_number(linno)
                    break
            if not found:
                trio = Trio(word.lower(), linno)
                words.append(trio)
        linno += 1
    for item in words:
        print item.get_word(), item.get_amount(), item.get_lines()


main('./words.txt')