import json
#Reading teh file
file=open("../assets/quotes.txt")
content=file.read()
print(content)

#Writing teh file
authorQuote="Time and Tide waits for None"
file_path="../assets/quotes.txt"
with open(file_path,'ab') as f:
    f.write(authorQuote)


# WORKING WITH JSON




