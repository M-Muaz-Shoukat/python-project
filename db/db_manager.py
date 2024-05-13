import json

class DBManager:
    @staticmethod
    def read(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def save(filename,data):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

