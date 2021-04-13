import re

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent ALice gave the secret documents to Agent Bob.')
mo2 = namesRegex.sub('PENIS', 'Agent ALice gave the secret documents to Agent Bob.')


namesRegex2 = re.compile(r'Agent (\w)\w*')
mo3 = namesRegex2.findall('Agent ALice gave the secret documents to Agent Bob.')


print(namesRegex.findall('Agent ALice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('PENIS', 'Agent ALice gave the secret documents to Agent Bob.'))
print(namesRegex2.findall('Agent ALice gave the secret documents to Agent Bob.'))
print(namesRegex2.sub(r'Agent \1****', 'Agent ALice gave the secret documents to Agent Bob.'))