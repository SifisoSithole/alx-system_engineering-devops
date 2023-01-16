#!/usr/bin/python3
"""
Script that returns information from an api
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(sys.argv[1])
    req = requests.get(url)
    tasks = []
    task_st = []
    for task in req.json():
        task_st.append(task.get('completed'))
        tasks.append(task.get('title'))
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    req = requests.get(url)
    name = req.json().get('username')

    dict_list = []
    for i in range(len(task_st)):
        my_dict = {}
        my_dict.update({"task": tasks[i], "completed": task_st[i], "username": name})
        dict_list.append(my_dict)

    with open("{}.json".format(sys.argv[1]), "w") as f:
        json.dump({"{}".format(str(sys.argv[1])): dict_list}, f)
