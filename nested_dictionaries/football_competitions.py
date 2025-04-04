import requests

url = "http://api.football-data.org/v4/competitions/"

response_API = requests.get(url)

print(response_API.status_code)

football_data = response_API.json()

print(football_data)

football_data.keys()

football_data['competitions']

competition_names_list = []

for competition in football_data['competitions']:
    name = competition['name']
    competition_names_list.append(name) 

print(competition_names_list)

print(len(competition_names_list))

distinct_competition_names = set(competition_names_list)

competition_names = list(set(competition_names_list))

print(competition_names)

print(len(competition_names))
