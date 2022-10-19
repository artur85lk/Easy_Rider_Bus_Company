import json
import re

DEBUG = False
date = ""
if DEBUG:
    date = [
        {"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": 8.12},
        {"bus_id": 128, "stop_id": 3, "stop_name": "", "next_stop": 5, "stop_type": "", "a_time": "08:19"},
        {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"},
        {"bus_id": 128, "stop_id": "7", "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F",
         "a_time": "08:37"},
        {"bus_id": "", "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": ""},
        {"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"},
        {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "",
         "a_time": "09:59"},
        {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": "0", "stop_type": "F",
         "a_time": "10:12"},
        {"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S",
         "a_time": "08:13"},
        {"bus_id": "512", "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": 5,
         "a_time": "08:16"}]
else:
    date = input()
y = json.loads(date)

bus_id = 0
stop_id = 0
stop_name = 0
next_stop = 0
stop_type = 0
a_time = 0
error = 0

for i in range(0, len(y)):
    if isinstance(y[i]['bus_id'], str):  # musi być int
        bus_id += 1
        error += 1
    if isinstance(y[i]['stop_id'], str):  # musi być int
        stop_id += 1
        error += 1
    if y[i]['stop_name'] == "" or isinstance(y[i]['stop_name'], int) or isinstance(y[i]['stop_name'], float):
        stop_name += 1
        error += 1
    if isinstance(y[i]['next_stop'], str) or isinstance(y[i]['next_stop'], float):
        next_stop += 1
        error += 1

    if y[i]["stop_type"] != "S" and y[i]["stop_type"] != "F" and y[i]["stop_type"] != "O" and str(
            y[i]['stop_type']) != "":
        stop_type += 1
        error += 1
    print(y[i]["stop_type"])
    if not bool(re.match('\d\d:\d\d', str(y[i]['a_time']))):
        a_time += 1
        error += 1

print(f"Type and required field validation: {error} errors")
print("bus_id:", bus_id)
print("stop_id:", stop_id)
print("stop_name", stop_name)
print("next_stop", next_stop)
print("stop_type", stop_type)
print("a_time", a_time)
