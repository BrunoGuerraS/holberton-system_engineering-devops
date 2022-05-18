#!/usr/bin/python3
"""
Python script that, using this REST API
"""
import csv
import requests
from sys import argv
import json


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
            'task': str(argv[1]),
            'completed': str(todo.get('completed')),
            'username': str(user.get('username')),
        }
        list_todo.append(todo_csv)
        if todo.get('completed'):
            todok = todok + 1

    for item in list_todo:
        print(item)

    print(prompt.format(name, todok, len(todos)))

    for todo in todos:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))

    dic_worker_json = {}
    dic_worker_json[argv[1]] = list_todo
    print(dic_worker_json)
    filename = "{}.json".format(argv[1])
    with open(filename, 'w') as file:
        json.dump(dic_worker_json, file)


if __name__ == "__main__":
    gather()
