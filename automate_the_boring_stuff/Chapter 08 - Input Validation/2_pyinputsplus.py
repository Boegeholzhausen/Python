import pyinputplus as pyip

pyip.RetryLimitException

response = pyip.inputInt(timeout=5, prompt='Enter a number: ', min=5, lessThan=6)
print(response)

pyip.TimeoutException

response2 = pyip.inputInt(limit=5, prompt='Enter a number: ', greaterThan=5)
print(response2)

reply = pyip.inputStr(prompt="WAS GEEEEEHT?: ")
print(reply)