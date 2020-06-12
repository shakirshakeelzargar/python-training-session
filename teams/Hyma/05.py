import requests
author = input("Hi, Welcome to Quotes World \n Please enter the name of the author:")

def jsonDownload(author):
    quotePath = 'https://api.quotable.io/quotes?author='+author
    #requests.get('https://api.quotable.io/quotes?author={author}')
    print('url:', quotePath)
    url = requests.get(quotePath)
    return (f"{url.json()}")

print("Enjoy the Quotes of {author}:", jsonDownload(author))


