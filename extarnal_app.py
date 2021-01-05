import json
import urllib.request as request
import numpy as np
from datetime import datetime

with request.urlopen("http://127.0.0.1:8000/workers/jsonworkers/") as response:
    source = response.read()
    data = json.loads(source)

# print(data)
salary_list = []
for dict in data:
    for key, value in dict.items():
        if key == "SALARY":
            salary_list.append(value)
print(salary_list)
np.set_printoptions(linewidth=np.inf)
salary_arr = np.array(salary_list)
salary_num = np.array(salary_arr).astype(np.float)
salary_avg = np.average(salary_num)
print(salary_avg)

more_year =[]
for dict in data:
    for key, value in dict.items():
        if key == "HIRE_DATE":
            if (datetime.strptime(value, '%Y-%m-%d')) < datetime(2020, 1, 5):
                more_year.append(dict)

poor_list=[]
for poor in more_year:
    for key, value in poor.items():
        if key == "SALARY":
            if (float(value)) < salary_avg:
                poor_list.append(poor)
with open('file.txt', 'w') as file:
    file.write(json.dumps(poor_list))


