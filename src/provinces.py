import json


def process_provinces(data):
    return (
        {'name': province.get('name'), 'code': province.get('code')}
        for province in data
    )


with open('data/vietnam_nested.json', 'r') as f:
    data = json.load(f)
    list_province = process_provinces(data)
