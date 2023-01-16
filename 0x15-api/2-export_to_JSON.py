#!/usr/bin/python3
"""
Script that returns information from an api
"""

import json
import requests
from sys import argv

def write_json(a):
    url = 'https://jsonplaceholder.typicode.com/users/%s/todos' % a
    req = requests.get(url)
    tasks = []
    task_st = []
    for task in req.json():
        task_st.append(task.get('completed'))
        tasks.append(task.get('title'))
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(a)
    req = requests.get(url)
    name = req.json().get('username')

    dict_list = []
    for i in range(len(task_st)):
        my_dict = {}
        my_dict.update({"task": tasks[i], "completed": task_st[i],
                        "username": name})
        dict_list.append(my_dict)

    with open("{}.json".format(a), "w") as f:
        json.dump({"{}".format(a): dict_list}, f)

if __name__ == "__main__":
    write_json(argv[1])
