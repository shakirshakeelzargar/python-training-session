import json
import requests
import xlsxwriter


author_name=input("Plse enter author name : \n")
author=author_name
def pull_data_from_api(author):
    """
    pull_from_api() function takes one arugument and pulling authors data from api
    """
    URL="https://api.quotable.io/quotes?author"
    PARAMS={"name":author}
    req=requests.get(url = URL, params=PARAMS)
    json_data=req.json()
    return json_data

def get_json_data(pull_data_from_api,author_name):
    '''
    Creating author name as a json file
    '''
    file_path=f"{author_name}.json"
    with open(file_path, "w") as jf:
        json.dump(pull_data_from_api(author_name),jf,indent=4)
    return file_path

file_path=get_json_data(pull_data_from_api,author) 
def read_json_file(filepath):
    '''
    read_json_file() takes one arugument,returns quotes list from json data
    '''
    with open(filepath, "r") as read_file:
        data = json.load(read_file)
        results=data.get("results",None)
        res_list=results[:]
        res = [ sub['content'] for sub in res_list ] 
    return res

filepath=read_json_file(file_path)

def printing_quotes_excel(data):
    '''
    printing_quotes_excel() takes one arugument and prints quotes in excel file
    '''
    workbook = xlsxwriter.Workbook('quotes.xlsx') 
    worksheet = workbook.add_worksheet() 
    row = 0
    column = 0
    for item in data : 
        worksheet.write(row, column, item) 
        row += 1
    workbook.close() 
printing_quotes_excel(filepath)

        
        



