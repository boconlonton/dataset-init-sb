import json
import itertools


def process_districts(data):
    for province in data:
        yield [
            {'disctrict_name': district.get('name'),
             'district_code': district.get('code'),
             'province_code': province.get('code')}
            for district in province.get('districts')
        ]


with open('data/vietnam_nested.json', 'r') as f:
    data = json.load(f)
    list_district = process_districts(data)
    for item in itertools.islice(list_district, 0, 5):
        print(list(item))
