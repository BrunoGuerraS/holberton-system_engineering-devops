#!/usr/bin/python3
"""
Python script that, using this REST API
"""
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
    for todo in todos:
        if todo.get('completed'):
            todok = todok + 1
    print(prompt.format(name, todok, len(todos)))
    for todo in todos:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))


if __name__ == "__main__":
    gather()
