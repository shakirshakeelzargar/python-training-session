#!/usr/local/bin/python3
import requests
import json
#author = input("Hi, Welcome to Quotes World \n Please enter the name of the author:")

def jsonDownload(author):
    quotePath = 'https://api.quotable.io/quotes?author='+author
    #requests.get('https://api.quotable.io/quotes?author={author}')
    print('url:', quotePath)
    url = requests.get(quotePath)
    return url.json() #(f"{url.json()}")

#jsonResult=jsonDownload(author)
#for item in jsonResult["results"]:
 #   print(item)

def downloadAllAuthors():
    authors=["gandhi","nehru","abraham"]
    for author in authors:
        result=jsonDownload(author)
        filepath=f"{author}.json"
        with open(filepath,"w") as authorFile:
            #json.dump(result,filepath)
            authorFile.write(json.dumps(result))

downloadAllAuthors()

#Images/Sub1/Sub2/

