# API: Random user Generator
* [Random user generator](https://randomuser.me/ "Random user generator : Open source API for fake user data.")
    * This API provides us with the data to ingest.

## Setting up API for ingestion. 

```
def ingest() -> dict:
    import requests
    import json 
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res
```

* The above code uses `requests` for requesting data from the API and `json` for parsing the obtained data. 

The obtained response is of the form:

```
{
    "gender": "male",
    "name": {
        "title": "Mr",
        "first": "Dejan",
        "last": "\u0110oki\u0107"
    },
    "location": {
        "street": {
            "number": 4875,
            "name": "Ilije \u010cali\u0107a"
        },
        "city": "Mitrovica",
        "state": "Rasina",
        "country": "Serbia",
        "postcode": 98516,
        "coordinates": {
            "latitude": "55.8682",
            "longitude": "-68.6121"
        },
        "timezone": {
            "offset": "+11:00",
            "description": "Magadan, Solomon Islands, New Caledonia"
        }
    },
    "email": "dejan.dokic@example.com",
    "login": {
        "uuid": "22f748bf-8ded-4099-a67c-3940a675ea4a",
        "username": "heavypeacock287",
        "password": "gagging",
        "salt": "FZ51cJLy",
        "md5": "89100bf18334c94e6fc579c57ba18ca9",
        "sha1": "d6c3fd5fa6789a11d3c7e91c9fb54d8abac04b0c",
        "sha256": "553d35617014e38cf95a556f11a48f5d60fa42d0812e8deced535a3e5a9278b4"
    },
    "dob": {
        "date": "1979-12-03T17:51:38.001Z",
        "age": 44
    },
    "registered": {
        "date": "2007-08-19T00:21:08.228Z",
        "age": 16
    },
    "phone": "034-4386-262",
    "cell": "064-0742-168",
    "id": {
        "name": "SID",
        "value": "822342846"
    },
    "picture": {
        "large": "https://randomuser.me/api/portraits/men/5.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/5.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/5.jpg"
    },
    "nat": "RS"
}
```

to format the data,

```
def format(res) -> dict:
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['phone'] = res['phone']
    data['email'] = res['email']
    data['address'] = f"{location['street']['number']}, {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['username'] = res['login']['username']
    data['password'] = res['login']['password']
    data['dob'] = res['dob']['date']
    data['registered'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data
```


