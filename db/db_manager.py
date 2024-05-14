import json

class DBManager:
    @staticmethod
    def read(**kwargs):
        file_path = kwargs.get('file_path')
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def save(**kwargs):
        file_path = kwargs.get('file_path')
        data = kwargs.get('data')
        try:
            existing_data = DBManager.read(file_path=file_path)
        except FileNotFoundError:
            existing_data = []
        existing_data.append(data)

        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)

    @staticmethod
    def update(**kwargs):
        file_path = kwargs.get('file_path')
        id = kwargs.get('id')
        data = kwargs.get('data')
        existing_data = DBManager.read(file_path=file_path)
        if 0 <= id < len(existing_data):
            existing_data[id] = data
            with open(file_path, 'w') as f:
                json.dump(existing_data, f, indent=4)
            return True
        else:
            return False
    
    @staticmethod
    def delete(**kwargs):
        file_path = kwargs.get('file_path')
        id = kwargs.get('id')
        existing_data = DBManager.read(file_path=file_path)
        if 0 <= id < len(existing_data):
            del existing_data[id]
            with open(file_path, 'w') as f:
                json.dump(existing_data, f, indent=4)
            return True
        else:
            return False
