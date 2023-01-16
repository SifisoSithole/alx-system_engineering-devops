#!/usr/bin/python3
"""
Script that returns information from an api
"""

if __name__ == "__main__":
    write_json = __import__('2-export_to_JSON').write_json
    import os
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/users'
    req = requests.get(url)
    u = req.json()
    for user in u:
        write_json(user.get('id'))
    my_dict = {}
    for user in u:
        name = '{}.json'.format(user.get('id'))
        with open(name, 'r') as f:
            my_dict.update(json.load(f))
        os.remove(name)
    with open('todo_all_employees.json', 'w') as f:
        json.dump(my_dict, f)
