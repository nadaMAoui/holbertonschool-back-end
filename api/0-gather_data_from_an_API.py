#!/usr/bin/python3
"""
gather_data_from_an_API
"""
import requests
import sys

employee_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/todos?userId=" + str(employee_id)

response = requests.get(url)

if response.status_code != 200:
    print("Error: Could not retrieve TODO list for employee ID", employee_id)
    sys.exit(1)

todos = response.json()

completed_tasks = []
total_tasks = len(todos)

for todo in todos:
    if todo["completed"]:
        completed_tasks.append(todo["title"])

num_completed_tasks = len(completed_tasks)

employee_name = todos[0]["userId"]
url = "https://jsonplaceholder.typicode.com/users/" + str(employee_name)

response = requests.get(url)
if response.status_code != 200:
    print("Error: Could not retrieve employee name for ID", employee_name)
    sys.exit(1)

employee_data = response.json()
employee_name = employee_data["name"]

print("Employee", employee_name, "is done with tasks({}/{}):".format(num_completed_tasks, total_tasks))

for task in completed_tasks:
    print("\t", task)
