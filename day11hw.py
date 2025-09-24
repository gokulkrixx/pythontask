from datetime import datetime
import json
from tracker import travel_record

travel =[
    travel_record("paris","City of lights", "04/01/2024"),
    travel_record("Rome"," power for the Roman Empire", "02/03/2025"),
    travel_record("Agra"," Taj mahal", "02/03/2025")
]

for trip in travel:
    date = datetime.strptime(trip["date"],"%d/%m/%Y")
    trip["date"] = date.strftime("%B %d,%Y")

json_str = json.dumps(travel)
print(f"""json string format
_____________________
{json_str}
""")

json_format = json.loads(json_str)

print("Printing in json format")
print("")
for dict in json_format:
    for x,y in dict.items():
        print (f"""{x}: {y}""")
    print("___________________")