import re
phoneNumRegex = re.compile(r'd\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 415-555-4242")
