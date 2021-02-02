#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""
import json
import requests

if __name__ == "__main__":
        set_id = set()
        request = requests.get("https://jsonplaceholder.typicode.com/posts")
        data = request.json()
        for user in data:
                set_id.add(user.get("userId"))
        file_export = {}
        url = "https://jsonplaceholder.typicode.com/users/{}"
        url1 = "https://jsonplaceholder.typicode.com/todos?userId={}"
        for user in set_id:
                rq_users = requests.get(url.format(user))
                rq_name = rq_users.json().get("username")
                rq_users = requests.get(url1.format(user))
                data_request = rq_users.json()
                file_export['{}'.format(user)] = []
                for task in data_request:
                        file_export['{}'.format(user)].append({
                                "task": task.get('title'),
                                'completed': task.get('completed'),
                                'username': rq_name
                        })
        with open('todo_all_employees.json', mode='w') as file:
                json.dump({int(x): file_export[x] for x in file_export.keys()},
                          file, sort_keys=True)
