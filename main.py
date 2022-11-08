import json

date = input()

y = json.loads(date)

key_bus_id = {}
for i in y:
    if i["stop_type"] == "":
        i["stop_type"] = "J"
    try:
        if key_bus_id[i["stop_name"]]:
            key_bus_id[i["stop_name"]] = key_bus_id[i["stop_name"]] + i["stop_type"]
    except:
        key_bus_id[i["stop_name"]] = i["stop_type"]
finish = []

for k, v in key_bus_id.items():
    if len(v) > 1 and v[0] != v[1]:
        if v[0] == "O" or v[1] == "O":
            finish.append(k)
print("On demand stops test:")
result = set(finish)
result = sorted(list(result), reverse=False)
if len(result):
    print(f"Wrong stop type: {result}")
else:
    print("OK")
