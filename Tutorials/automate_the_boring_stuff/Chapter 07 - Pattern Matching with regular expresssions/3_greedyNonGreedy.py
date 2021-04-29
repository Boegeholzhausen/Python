import re

greedyRegex = re.compile(r'(\d){3,5} ')
mo = greedyRegex.search("12345")
print(mo.group())

nogreedyRegex = re.compile(r'(\d){3,5}?')
mo = nogreedyRegex.search("12345")
print(mo.group())