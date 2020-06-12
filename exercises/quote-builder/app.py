
from google.oauth2.service_account import Credentials
import gspread
import sys

from quoteClient import getQuotesByAuthor

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credentials = Credentials.from_service_account_file(
    '/projects/freelancing/training/python-training-session/keys/rafa-dev-e8d080821d26.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)


#sh = gc.create("Example spreadsheet1")
sh = gc.open("Example spreadsheet1")
#sh.share('nirmalk.web@gmail.com', perm_type='user', role='writer')

#sh.sheet1.update('A1', [[1, 2], [3, 4]])

# Or update a single cell
#sh.sheet1.update('B42', "it's down there somewhere, let me take another look.")


def pushToSheet(spFile,sheetName,dataList):
    #Create a Sheet
    worksheet = spFile.add_worksheet(title=sheetName,rows="100", cols="20")
    worksheet.update('A1', [["Quotes"]])
    worksheet.format('A1:B1', {'textFormat': {'bold': True}})
    ictr=1;
    for data in dataList:
        print(data)
        ictr=ictr+1;
        worksheet.update('A' + str(ictr), [[data["content"]]])



def saveToSheets(authors):
    for author in authors:
        response=getQuotesByAuthor(author)
        pushToSheet(sh,author,response["results"])

saveToSheets(["gandhi","nehru","abraham"]);