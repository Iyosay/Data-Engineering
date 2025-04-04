import requests

url = "https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo"

response_API = requests.get(url)

print(response_API.status_code)

print(response_API)

get_data = response_API.json()

print(get_data)

print(get_data.keys())

job_data = get_data['jobs']

len(get_data['jobs'])

job_data[0]

job_data[0]['jobTitle']

senior_role_list = []

manager_role_list = []

for jobs in job_data:
    role_list = jobs['jobTitle']
    if "Senior" in role_list:
        print(role_list)

for jobs in job_data:
    if 'Senior' in jobs['jobTitle']:  
        senior_role_list.append(jobs['jobTitle'])
    if 'Manager' in jobs['jobTitle']: 
        manager_role_list.append(jobs['jobTitle']) 

print(senior_role_list)

print(manager_role_list)
