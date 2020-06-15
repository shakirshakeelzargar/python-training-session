import requests
import json
#author = input("Hi, Welcome to Quotes World \n Please enter the name of the author:")

def getQuotesByAuthor(author):
    quotePath = 'https://api.quotable.io/quotes?author='+author
    print('url:', quotePath)
    url = requests.get(quotePath)
    return url.json()