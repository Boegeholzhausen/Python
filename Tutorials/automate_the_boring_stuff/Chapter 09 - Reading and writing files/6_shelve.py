import shelve

shelveFile = shelve.open("mydata")
shelveFile['cats'] = ["Sophie", "pooka", "Simon"]
print(shelveFile['cats'])

print(list(shelveFile.keys())) 
print(list(shelveFile.values())) 