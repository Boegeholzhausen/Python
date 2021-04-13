#! python3

import re, pyperclip

# Create a reges for numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext.12345, x12345
((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-)                  # first separator
(\d\d\d)                  # first 3 digits
(-)                       # second separator
(\d\d\d\d)                # last 4 digits
((ext(\.)?\s|x)         # exteension word-part (optional)
(\d{2,5}))?             # exteension number-part (optional)
''', re.VERBOSE)


# Create a regex for email address
emailRegex = re.compile(r'''
# some.+_things@something.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name 
''', re.VERBOSE)


# Get the text off the clipboard
text = str(pyperclip.paste())

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)
 
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)


# TODO: Copy the extracted email/phone to the clipboard 


