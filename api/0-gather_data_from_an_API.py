#!/usr/bin/python3
"""
gather data from API
"""
import requests
import sys


if __name__ == '__main__':

    id = sys.argv[1]
    task_title = []
    complete = 0
    total = 0
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    result = requests.get(url_user).json()
    name = result.get('name')
    todos = "https://jsonplaceholder.typicode.com/todos/"
    res_task = requests.get(todos).json()
    for i in res_task:
        if i.get('userId') == int(id):
            if i.get('completed') is True:
                task_title.append(i['title'])
                complete += 1
            total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete, total))
    for x in task_title:
        print("\t {}".format(x))
