import json


date = input()
# date = [
#     {
#         "bus_id": 512,
#         "stop_id": 4,
#         "stop_name": "Bourbon Street",
#         "next_stop": 6,
#         "stop_type": "S",
#         "a_time": "08:13"
#     },
#     {
#         "bus_id": 512,
#         "stop_id": 6,
#         "stop_name": "Sunset Boulevard",
#         "next_stop": 0,
#         "stop_type": "F",
#         "a_time": "08:16"
#     }
# ]
# date = json.dumps(date)  # do testów

y = json.loads(date)
step = []

for i in y:
    step.append([i["stop_name"], i["a_time"], i["bus_id"]])
last_value = 0
counter = 0
good = True
rong_step = True
print(f"Arrival time test:")
for s, v, k in step:
    new_v = [int(v[0:2] + v[3:5]), k]
    if counter == 0:
        last_value = new_v
    if counter > 0 and last_value[0] > new_v[0] and new_v[1] == last_value[1] and rong_step:
        print(f"bus_id line {k}: wrong time on station {s}")
        good = False
        rong_step = False
    if new_v[1] != last_value[1]:
        rong_step = True
    last_value = new_v
    counter += 1
if good:
    print("OK")


