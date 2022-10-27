

import json
import re

date = input()
# date = json.dumps(date)  # do testów

y = json.loads(date)

line = {}
good = True

for i in y:
    line[i["bus_id"]] = ""
for i in y:
    line[i["bus_id"]] += i["stop_type"]
for k, v in line.items():
    if not bool(re.match(r'S.?.?.?.?F', v)):
        print(f"There is no start or end stop for the line: {k}.")
        good = False
# transfer
transfer = []
for i in y:
    more_two = 0
    for j in y:
        if j["stop_name"] == i["stop_name"]:
            more_two += 1
    if more_two > 1:
        transfer.append(i["stop_name"])
    more_two = 0

start = sorted(list(set([i["stop_name"] for i in y if i["stop_type"] == "S"])))
transfer = sorted(list(set(transfer)))
# transfer = [i["stop_name"] for i in y if not re.match(r'[FS]', i["stop_type"])]
finish = sorted(list(set([i["stop_name"] for i in y if i["stop_type"] == "F"])))
if good:
    print(f"Start stops: {len(start)} {start}")
    print(f"Transfer stops: {len(transfer)} {transfer}")
    print(f"Finish stops: {len(finish)} {finish}")
