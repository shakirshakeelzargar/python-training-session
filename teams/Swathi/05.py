import json
import requests
author_name=input("Plse enter author name : \n")

#def pull_the_data
author=author_name
URL="https://api.quotable.io/quotes?author"
PARAMS={"name":author}
req=requests.get(url = URL, params=PARAMS)
json_data=req.json()

def get_json_file(json_data,author_name):
    '''
    Creating author name as a json file
    '''
    file_path=f"./{author_name}.json"
    
    with open(file_path, "w") as jf:
        json.dump(json_data,jf)
    return file_path

file_path=get_json_file(json_data,author) 


def read_json_file(filepath):
    import json
    with open(filepath, "r") as read_file:
        data = json.load(read_file)
        results=data.get("results",None)
        res_list=results[:]
        
        



read_json_file(file_path)