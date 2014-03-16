import re
import collections
from operator import itemgetter, attrgetter

__author__ = 'Pedro'

#Class to hold word, line number list, amount found
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
    #A contiguous sequence of non-white-space characters defines a word so thats what our regex will be
    pattern = re.compile('\\S+')
    #Current line number to see where the word was found
    linno = 1
    #Go line by line searching and adding.  If repeated, increase amount and put line number where it is found
    for line in file:
        #print "Currentline:",line
        listofwords = pattern.findall(line)
        #print "List of matches",listofwords
        #Search each match to see if repeated or add new
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
    #Unsorted
    #for item in words:
    #    print  item.get_amount(), item.get_word(), item.get_lines()
    print 'Sorted:'
    s1 = sorted(words, key=attrgetter('word'))
    s = sorted(s1, key=lambda element: len(element.word))
    sortedlist = sorted(s,key=attrgetter('amount'), reverse=True)
    for item in sortedlist:
        print  item.get_amount(), item.get_word(), item.get_lines()


main('./words.txt')