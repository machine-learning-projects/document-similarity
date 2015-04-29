import re

# regular expression
# \w matches any alphanumeric character and the underscore
# + causes the RE to match 1 or more repetitions of the preceding RE
WORD = re.compile(r'\w+')

def textToVector(text):
    words = WORD.findall(text)
