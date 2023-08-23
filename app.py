import json , os ,time


def OS():
   code=os.system("cls")
   return code

def Time():
   code=time.sleep(3)
   return code

with open("data.json","r") as file:
    data=json.load(file)
    
#print(json.dumps(data,indent=2))

print("__CONSOLE DICTIONARY__")
print()
print("Search Word")
word=input("> ").lower()
if word not in data:
    print("Word not found in the dictionary")
    Time()
    OS()
else:

  print(data[word])
  Time()
  OS()