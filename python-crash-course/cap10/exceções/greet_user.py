import json


def greet_user(filename):
    with open(filename) as file_object:
        username = json.load(file_object)
        print("Welcome back", username)


filename = "username.json"
greet_user(filename)
