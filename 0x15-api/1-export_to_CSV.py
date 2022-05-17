#!/usr/bin/python3
"""
Python script that, using this REST API
"""
import csv
import requests
from sys import argv


def gather():
    """ get date from api """
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users?id={}".format(url, argv[1])).json()[0]
    todos = requests.get("{}/todos?userId={}".format(url, argv[1])).json()
    name = user.get("name")
    todok = 0
    prompt = "Employee {} is done with tasks({}/{}):"
    list_todo = []

    for todo in todos:
        todo_csv = {
            'USER_ID': argv[1],
            'USERNAME': name,
            'TASK_COMPLETED_STATUS': str(todo.get('completed')),
            'TASK_TITLE': str(todo.get('title'))
        }
        list_todo.append(todo_csv)
        if todo.get('completed'):
            todok = todok + 1

    print(prompt.format(name, todok, len(todos)))

    for todo in todos:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))

    filename = "{}.csv".format(argv[1])
    colums = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=colums, quoting=csv.QUOTE_ALL)
        writer.writerows(list_todo)


if __name__ == "__main__":
    gather()
