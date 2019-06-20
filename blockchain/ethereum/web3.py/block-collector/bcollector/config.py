import os
import json


class FileConfig(object):
    def __init__(self, filename="conf/config.json"):
        self.is_prod = False
        self.config = {}

        try:
            if (os.environ["PYTHON_ENV"] == "production"):
                self.is_prod = True
        except KeyError:
            self.is_prod = False

        with open(filename) as f:
            file_contents = f.read()
            json_contents = json.loads(file_contents)
            if self.is_prod:
                self.config = json_contents["prod"]
            else:
                self.config = json_contents["dev"]

    def get_web3(self):
        return self.config["web3"]

    def get_database(self):
        return self.config["database"]
