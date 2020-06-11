import json

def getQuotes():
    """
    Returns list of quotes
    """
    jsonFilePath="../assets/quotes.json"
    file=open(jsonFilePath)
    quotesList=json.load(file)
    return quotesList

def writeToQuotesFile(filepathname,originalList):
    jsonContent=json.dumps(originalList)
    with open(filepathname,"wb") as file:
        file.write(jsonContent)

def addQuote(quoteInfo,originalList):
    newList=originalList
    newList["quotes"].append(quoteInfo)
    return newList

def displayQuotes(bannerName,quoteList):
    print(bannerName)
    for item in quoteList["quotes"]:
        result="{}:{}".format(item["author"].encode('utf-8'),item["quote"].encode('utf-8'))


def getQuotesManual():
    """
    Returns list of quotes
    """
    jsonContent={}
    jsonFilePath="../assets/quotes.json"
    with open(jsonFilePath) as f:
        jsonContent=f.read()

    quotesList=json.loads(jsonContent)
    return quotesList


def run():
    jsonFilePath="../assets/quotes.json"
    dataList=getQuotes();
    displayQuotes("Before Adding",dataList)
    quoteObject={"author":"MKGandhi","quote":"Change is Constant"}
    newList=addQuote(quoteObject,dataList)
    writeToQuotesFile(jsonFilePath,newList)
    displayQuotes("After Adding",newList)

run();


requests