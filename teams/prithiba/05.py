import json
f = open('gandhiji.json',) 
content=f.read()
print(content)
#data = json.load(f) 
#for i in data['results']: 
#   print(i) 
f.close()