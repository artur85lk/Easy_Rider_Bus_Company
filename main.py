import json


date = input()
y = json.loads(date)


bus_stops = []

for i in range(0, len(y)):
    bus_stops.append(y[i]['bus_id'])

print(bus_stops)
bus_s_set = set(bus_stops)
print("Line names and number of stops:")
for i in bus_s_set:
    print(f"bus_id: {i}, stops: {bus_stops.count(i)}")


