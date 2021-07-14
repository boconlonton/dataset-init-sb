import json


with open('data/country.json', 'r') as f:
    data = json.load(f)
    for i in range(5):
        print(data[i])
