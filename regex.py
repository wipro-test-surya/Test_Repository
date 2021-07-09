import re
import json

txt = "The rain in Spain"
x = re.split(' ',txt)
# print(x)


with open('file.json','r') as file:
    data = json.load(file)
    # print(data)
    values = []

    print(data)
    a = list(data.values())
    values.append(a[2]))
        
