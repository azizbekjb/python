#Amaliyot10.4.1
#1
import json
data = {
    'Model' : 'Malibu',
    "Rang" : 'Qora',
    'Yil' : 2020,
    'Narx' : 4000
}
data_json = json.dumps(data, indent=4)
print(data_json)
#Natija:
    # {
    #     "Model": "Malibu",
    #     "Rang": "Qora",
    #     "Yil": 2020,
    #     "Narx": 4000
    # }
