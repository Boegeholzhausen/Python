from selenium import webdriver

browser = webdriver.Chrome(r"C:\PythonCommands\chromedriver.exe")
browser.get("https://10fastfingers.com/typing-test/german")

browser.find_element_by_id("auswertung-result")

print(browser.title)