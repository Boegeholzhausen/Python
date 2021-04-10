import re

phoneNumRegex = re.compile(r'Hallo')

message = 'My Hallo is 415-555-4242'

print(phoneNumRegex.findall(message))