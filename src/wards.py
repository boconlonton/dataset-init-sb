import json
import itertools


def process_wards(data):
    for ward in data:
        temp = {
            'ward_name': ward.get('ward_name'),
            'ward_code': ward.get('ward_code'),
            'district_code': ward.get('district_code')
        }
        yield temp


with open('data/vietnam_flat.json', 'r') as f:
    data = json.load(f)
    list_district = process_wards(data)
    for item in itertools.islice(list_district, 100, 105):
        print(item)
