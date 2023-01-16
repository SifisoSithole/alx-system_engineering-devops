#!/usr/bin/python3
"""
Script that returns information from an api
"""

if __name__ == "__main__":
    import requests
    import sys

    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
    req = requests.get(url)
    tasks = []
    task_st = []
    for task in req.json():
        task_st.append(task.get('completed'))
        tasks.append(task.get('title'))
    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    req = requests.get(url)
    name = req.json().get('username')

    with open(f'{sys.argv[1]}.csv', 'w') as f:
        for i in range(len(task_st)):
            m = f'"{sys.argv[1]}","{name}","{task_st[i]}","{tasks[i]}"\n'
            f.write(m)
