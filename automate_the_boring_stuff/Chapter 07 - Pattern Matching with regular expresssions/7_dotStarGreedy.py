import re

text = "< Hallo > Haha >\n penis>"

nongreedy = re.compile(r"<(.*?)>")
nongreedyvar = nongreedy.findall(text)
print(nongreedyvar)

greedy = re.compile(r"<(.*)>")
greedyvar = greedy.findall(text)
print(greedyvar)

alle = re.compile(r"<(.*)>", re.DOTALL)
alle = alle.findall(text)
print(alle)