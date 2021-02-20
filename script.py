import json
from os import write
import xmltodict

def read_file(file):
    with open(file) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()
        return data_dict

def create_and_write_json(dict):
    json_data = json.dumps(dict)

    with open('data.json', 'w') as json_file:
        json_file.write(json_data)
        json_file.close()


