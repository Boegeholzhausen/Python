import re


message = "My number is 415-555-4242. number is 415-555-5555."

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")


mo = phoneNumRegex.search(message)
print(mo.group(0))
print(phoneNumRegex.findall(message))

message2 = "hahaha"   
message3 = "hahahaha"     
haRegex = re.compile(r'(ha){3,8}')
mo2 = haRegex.search(message2)
mo3 = haRegex.search(message3)

print(mo2.group())
print(mo3.group())
