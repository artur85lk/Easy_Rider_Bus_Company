import json
import re

DEBUG = True
date = ""
if DEBUG:
    # date = [
    #     {"bus_id": 128, "stop_id": 1, "stop_name": "Fifth Avenue", "next_stop": 4, "stop_type": "S", "a_time": "08:12"},
    #     {"bus_id": 128, "stop_id": 4, "stop_name": "abbey Road", "next_stop": 5, "stop_type": "FF", "a_time": "08:19"},
    #     {"bus_id": 128, "stop_id": 5, "stop_name": "Santa Monica Boulevard", "next_stop": 8, "stop_type": "O",
    #      "a_time": "two"},
    #     {"bus_id": 128, "stop_id": 8, "stop_name": "Elm Street Str.", "next_stop": 11, "stop_type": "",
    #      "a_time": "08:37"},
    #     {"bus_id": 128, "stop_id": 11, "stop_name": "Beale Street", "next_stop": 12, "stop_type": "",
    #      "a_time": "39:20"},
    #     {"bus_id": 128, "stop_id": 12, "stop_name": "Sesame Street", "next_stop": 14, "stop_type": "",
    #      "a_time": "09:95"},
    #     {"bus_id": 128, "stop_id": 14, "stop_name": "Bourbon street", "next_stop": 19, "stop_type": "O",
    #      "a_time": "09:59"},
    #     {"bus_id": 128, "stop_id": 19, "stop_name": "Avenue", "next_stop": 0, "stop_type": "F", "a_time": "10:12"},
    #     {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S",
    #      "a_time": "08.13"},
    #     {"bus_id": 256, "stop_id": 3, "stop_name": "Startowa Street", "next_stop": 8, "stop_type": "d",
    #      "a_time": "08:16"},
    #     {"bus_id": 256, "stop_id": 8, "stop_name": "Elm", "next_stop": 10, "stop_type": "", "a_time": "08:29"},
    #     {"bus_id": 256, "stop_id": 10, "stop_name": "Lombard Street", "next_stop": 12, "stop_type": "",
    #      "a_time": "08;44"},
    #     {"bus_id": 256, "stop_id": 12, "stop_name": "Sesame Street", "next_stop": 13, "stop_type": "O",
    #      "a_time": "08:46"},
    #     {"bus_id": 256, "stop_id": 13, "stop_name": "Orchard Road", "next_stop": 16, "stop_type": "",
    #      "a_time": "09:13"},
    #     {"bus_id": 256, "stop_id": 16, "stop_name": "Sunset Boullevard", "next_stop": 17, "stop_type": "O",
    #      "a_time": "09:26"},
    #     {"bus_id": 256, "stop_id": 17, "stop_name": "Khao San Road", "next_stop": 20, "stop_type": "o",
    #      "a_time": "10:25"},
    #     {"bus_id": 256, "stop_id": 20, "stop_name": "Michigan Avenue", "next_stop": 0, "stop_type": "F",
    #      "a_time": "11:26"},
    #     {"bus_id": 512, "stop_id": 6, "stop_name": "Arlington Road", "next_stop": 7, "stop_type": "s",
    #      "a_time": "11:06"},
    #     {"bus_id": 512, "stop_id": 7, "stop_name": "Parizska St.", "next_stop": 8, "stop_type": "", "a_time": "11:15"},
    #     {"bus_id": 512, "stop_id": 8, "stop_name": "Elm Street", "next_stop": 9, "stop_type": "", "a_time": "11:76"},
    #     {"bus_id": 512, "stop_id": 9, "stop_name": "Niebajka Av.", "next_stop": 15, "stop_type": "", "a_time": "12:20"},
    #     {"bus_id": 512, "stop_id": 15, "stop_name": "Jakis Street", "next_stop": 16, "stop_type": "",
    #      "a_time": "12:44"},
    #     {"bus_id": 512, "stop_id": 16, "stop_name": "Sunset Boulevard", "next_stop": 18, "stop_type": "",
    #      "a_time": "13:01"},
    #     {"bus_id": 512, "stop_id": 18, "stop_name": "Jakas Avenue", "next_stop": 19, "stop_type": "",
    #      "a_time": "14:00"},
    #     {"bus_id": 1024, "stop_id": 21, "stop_name": "Karlikowska Avenue", "next_stop": 12, "stop_type": "S",
    #      "a_time": "13:01"},
    #     {"bus_id": 1024, "stop_id": 12, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F",
    #      "a_time": "14:00:00"},
    #     {"bus_id": 1024, "stop_id": 19, "stop_name": "Prospekt Avenue", "next_stop": 0, "stop_type": "F",
    #      "a_time": "14:11"}]
    date = [
        {"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Av.", "next_stop": 3, "stop_type": "S", "a_time": "08:12"},
        {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "8:19"},
        {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "OO",
         "a_time": "08:25"},
        {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F",
         "a_time": "08:77"},
        {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S",
         "a_time": "09:20"},
        {"bus_id": 256, "stop_id": 3, "stop_name": "Elm", "next_stop": 6, "stop_type": "", "a_time": "09:45"},
        {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "A",
         "a_time": "09:59"},
        {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F",
         "a_time": "10.12"},
        {"bus_id": 512, "stop_id": 4, "stop_name": "bourbon street", "next_stop": 6, "stop_type": "S",
         "a_time": "38:13"},
        {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F",
         "a_time": "08:16"}]

    date = json.dumps(date)
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

bus_stops = []

for i in range(0, len(y)):

    # if isinstance(y[i]['bus_id'], str):  # musi być int
    #     bus_id += 1
    #     error += 1
    # if isinstance(y[i]['stop_id'], str):  # musi być int
    #     stop_id += 1
    #     error += 1
    # if y[i]['stop_name'] == "" or isinstance(y[i]['stop_name'], int) or isinstance(y[i]['stop_name'], float):  #
    #     stop_name += 1
    #     error += 1
    if not bool(re.search(r'([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$', str(y[i]['stop_name']))):  # |Avenue|Boullevard|Street or bool(re.match(r'[A-Z][a-z]+ [A-Z][a-z]+\.', str(y[i]['stop_name']))) or bool(re.match(r'[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+\.', str(y[i]['stop_name']))) or bool(re.match(r'[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+', str(y[i]['stop_name']))):  #
        stop_name += 1
        error += 1
    # if isinstance(y[i]['next_stop'], str) or isinstance(y[i]['next_stop'], float):
    #     next_stop += 1
    #     error += 1

    if y[i]["stop_type"] != "S" and y[i]["stop_type"] != "F" and y[i]["stop_type"] != "O" and str(
            y[i]['stop_type']) != "":  #
        stop_type += 1
        error += 1
    # print(y[i]["stop_type"])
    if not bool(re.match(r'[0-2]\d:[0-5]\d', str(y[i]['a_time']))) or bool(
            re.match(r'[0-2]\d:[0-5]\d:\d\d', str(y[i]['a_time']))):  #
        a_time += 1
        error += 1

print(f"Type and required field validation: {error} errors")
# print("bus_id:", bus_id)
# print("stop_id:", stop_id)
print("stop_name", stop_name)  #
# print("next_stop", next_stop)
print("stop_type", stop_type)  #
print("a_time", a_time)  #
