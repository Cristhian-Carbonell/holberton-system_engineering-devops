#!/usr/bin/python3
"""
Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
	url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
						.format(argv[1]))
	data_name = url.json().get('name')
	url = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
						.format(argv[1]))
	data = url.json()
	done = 0
	total = 0
	for task in data:
		total += 1
			if task.get("completed"):
				done += 1
	print("Employee {} is done with tasks({}/{}):".format(data_name, done, total))
	for task in data:
		if task.get("completed"):
			print("\t {}".format(task.get("title")))
