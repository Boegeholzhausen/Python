import re


message = "call me 555-555-5555 asdfkljasd 555-555-5566"

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

print(phoneNumRegex.findall(message))
        
