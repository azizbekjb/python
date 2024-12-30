import json

data = {
    "address_components": [
        {
            "long_name": "Almazar District",
            "short_name": "Almazar District",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Tashkent",
            "short_name": "Tashkent",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Tashkent Region",
            "short_name": "Tashkent Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Almazar District, Tashkent, Uzbekistan",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.3645355,
            "lng": 69.2281531
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}
kenglik = data['geometry']['location']['lat']
uzunlik = data['geometry']['location']['lng']
print(kenglik, uzunlik)
#Natija:
    # 41.3645355 69.2281531
