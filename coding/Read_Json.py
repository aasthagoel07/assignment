import json
import sys

with open(sys.argv[1]) as f:
  data = json.load(f)
for pro in data["products"]:
    pro["categories"] = ','.join(pro["categories"])
    pro["name"] = pro.pop("title")
    pro["twitter"] = pro.pop("twitter") if "twitter" in pro else ""
print(json.dumps(data["products"]))