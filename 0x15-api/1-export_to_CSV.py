#!/usr/bin/python3
"""
Script that returns information from an api
"""

if __name__ == "__main__":
    import requests
    from sys import argv as a

    url = 'https://jsonplaceholder.typicode.com/users/%s/todos' % a[1]
    req = requests.get(url)
    t = []
    task_st = []
    for task in req.json():
        task_st.append(task.get('completed'))
        t.append(task.get('title'))
    url = 'https://jsonplaceholder.typicode.com/users/%s' % a[1]
    req = requests.get(url)
    n = req.json().get('username')

    with open('{}.csv'.format(a[1]), 'w') as f:
        for i in range(len(task_st)):
            m = '"%s","%s","%s","%s"\n' % (a[1], n, task_st[i], t[i])
            f.write(m)
