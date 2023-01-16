#!/usr/bin/python3
"""
This script takes an employee ID and

returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import sys
    import requests

    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
    req = requests.get(url)
    com_tasks = []
    no = 0
    for task in req.json():
        if task.get('completed'):
            com_tasks.append(task.get('title'))
        no += 1
    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    req = requests.get(url)
    name = req.json().get('name')
    msg = f'Employee {name} is done with tasks({len(com_tasks)}/{no}:'
    print(msg)
    for task in com_tasks:
        print('\t ' + task)
