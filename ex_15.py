#!/usr/bin/python

import json

class Directory(object):

    def __init__(self):
        self.users = []

    def save_directory(self, filename):
        with open(filename, "w") as target:
            target.write(json.dumps(self.users))

    def load_directory(self, filename):
        with open(filename, "r") as target:
            self.users = json.loads(target.read())

    def add_user(self, name, address, phone, email):
        self.users.append({
            "name": name,
            "address": address,
            "phone": phone,
            "email": email
        })

    def get_data(self, name):
        matches = list(filter(lambda x: x["name"] == name, self.users))
        if matches:
            return matches[0]
        return {}
