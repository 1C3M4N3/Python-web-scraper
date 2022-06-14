import requests
import re

try: 
    userInput = str(input("what site would you like to crawl: "))
    strippedInput = userInput.strip()
    req = requests.get(strippedInput)
    req.status_code
    req.encoding
    req.text
    req.text.find('<a')
except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.TooManyRedirects:
    print("Too many redirects")
except requests.exceptions.RequestException as e:
    print("Error unknown")
finally:
    forty = re.findall(r'[\'\"]((?:https?|telnet|ldaps?|ftps?)\:\/\/[\w|\d|\.|\:]+\/?.*?)[\'\"]', req.text)
    seven = re.findall(r'[\'\"](?:(?!https?|telnet|ldaps?|ftps?))(\/?[\w|\d|\.]+)[\'\"]', req.text) 
    type(forty)
    type(seven)
    for (a, k) in zip(forty, seven):
        print("Direct Link: \n" + a, "\n Relative Paths: \n" + userInput + k)

    print("You just crawled, " + userInput)