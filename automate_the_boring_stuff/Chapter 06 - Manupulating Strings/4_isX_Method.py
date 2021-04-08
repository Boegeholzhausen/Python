var = "Spinat Salat"

print(var.istitle())
print(var.islower())
print(var.isupper())
print(var.isspace() or var.istitle())

spam = ", ".join(["dog", "cat", "tiger"])
print(spam)

spam2 = "Hello World in the House"
newSpam = spam2.split()
print(newSpam)

spam2, sep, spam3 = "Hello World!".partition(" ")
print(spam2 + "trennen" +spam3)


spam4 = "HalloWorld"
print(spam4.center(30, "="))
print(spam4.rjust(30, "="))
print(spam4.ljust(30, "="))