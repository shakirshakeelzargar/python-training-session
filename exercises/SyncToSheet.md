# Title : SyncToSheet

Objective :
- We need to download the quotes from the Quotes API and Save them too Google Sheet
- We need to Programmtically Create a Spreadsheet
- Create Separate Tab Sheet for each Authors in the Google Sheet
- Once Done, Print the Spreadsheet Url.

Implementation Plan :

- You can't talk to Google Sheet API. What i need for this?
- I need a Service Account. Google Deprecated all the Calls to use directly username and password.
- Service Accounts (Virtual User)
 : Industry Standard to Execute Code on Behalf of Someone

Steps :
1. Create a Service Account. Login to Google Cloud to get the Service Key TOKEN : Done
2. We need to talk to API. REST API
3. SDK's : (REST API): google-sdk
4. Community package is available to talk to Spreadsheet API ?
5. Pip install packageName



Code Execution Plan :
- Create a SpreadSheet Utility to talk to Google Spreadhsheet
- Use Requests Library to Pull json from Author api
- Save the JSON data back to Spreadsheet via api
- Print the Url