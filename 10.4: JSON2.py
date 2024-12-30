#10.4: JSON
#JSON - JavaScript Object Notation
#json.dumps()
import json
bemor = {
    'ism' : 'Alijon Valiyev',
    'yosh' : 20,
    'oila' : True,
    "farzandlar" : ("Ahmad", "Bonu"),
    'allergiya' : None,
    "dorilar" : [
        {'nomi' : 'Analgin', 'miqdori' : 0.5},
        {'nomi' : 'Panadol', 'miqdori' : 1.2}
    ]
}
bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)
#Natija:JSON formatdagi fayl
    # {
    #     "ism": "Alijon Valiyev",
    #     "yosh": 20,
    #     "oila": true,
    #     "farzandlar": [
    #         "Ahmad",
    #         "Bonu"
    #     ],
    #     "allergiya": null,
    #     "dorilar": [
    #         {
    #             "nomi": "Analgin",
    #             "miqdori": 0.5
    #         },
    #         {
    #             "nomi": "Panadol",
    #             "miqdori": 1.2
    #         }
    #     ]
    # }
