"""Lab 1
"""
from mrjob.job import MRJob
import re

#this is a regular expression that finds all the words inside a String
WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class Lab1, that extends the MRJob format.
class Lab1(MRJob):

# this class will define two additional methods: the mapper method goes here
    def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (word.lower(), 1)

#and the reducer method goes after this line
    def reducer(self, word, counts):
        num = sum(counts)
        yield (word, num)
        #you have to implement the body of this method. Python's sum() function will probably be useful

#this part of the python script tells to actually run the defined MapReduce job. Note that Lab1 is the name of the class
if __name__ == '__main__':
    Lab1.run()
