import requests

url = "https://randomuser.me/api/?results=500"

response_API = requests.get(url)

print(response_API.status_code)

data = response_API.json()

print(data)

data.keys()

data['results']

informations = data['results']

females = []

males = []

for information in informations:
    if information['gender'] == 'female': 
        females.append(information)  
    elif information['gender'] == 'male':  
        males.append(information) 

print(females)

print(males)

for information in informations:
    print(information['dob']) 

for information in informations:
    print(information['dob']['date'])

dates = []

for information in informations:
    dates.append(information['dob']['date']) 

print(dates)

for information in informations:
    print(information['name']['first'])

for information in informations:
    print(information['name']['last'])

full_names= []

for information in informations:
    full_names.append(information['name']['first'] + " " + information['name']['last'])

print(full_names)
