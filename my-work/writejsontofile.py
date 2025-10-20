# playing with json
# Author: Marcin Kaminski

import json
data = {
    'name':'joe',
    'age':21,
    'student':True,
}

with open("silly.json", "w") as fp:
    json.dump(data,fp)
jsonSting = json.dumps(data)
print(data)
print(jsonSting)
