import yaml
import sys
import json

with open(sys.argv[1], 'r') as stream:
    data_loaded = yaml.safe_load(stream)
    for data in data_loaded:
        data["categories"] = data.pop("tags")
    print(json.dumps(data_loaded))
