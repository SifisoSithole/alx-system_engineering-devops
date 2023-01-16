#!/usr/bin/python3
"""
Script that returns information from an api
"""

if __name__ == "__main__":
    import requests
    from sys import argv as a

    url = 'https://jsonplaceholder.typicode.com/users/%s/todos' % a[1]
    req = requests.get(url)
    com_tasks = []
    no = 0
    for task in req.json():
        if task.get('completed'):
            com_tasks.append(task.get('title'))
        no += 1
    url = 'https://jsonplaceholder.typicode.com/users/%s' % a[1]
    req = requests.get(url)
    name = req.json().get('name')
    n = len(com_tasks)
    msg = 'Employee %s is done with tasks(%d/%d):' % (name, n, no)
    print(msg)
    for task in com_tasks:
        print('\t ' + task)
