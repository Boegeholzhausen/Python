spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = "hallo"

print(spam)
print(id(cheese[1]))
