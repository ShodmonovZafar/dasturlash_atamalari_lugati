import json

path_to_the_json_file = "json_files/dasturlash_atamalari_lugati.json"

with open(path_to_the_json_file, 'r') as f:
    data = json.load(f)

