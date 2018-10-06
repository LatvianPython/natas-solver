import json


def save_credentials(level, password):
    username = 'natas{}'.format(level)
    level = str(level)
    if password is None:
        return
    with open('credentials.json', 'r+', encoding='utf-8') as file:
        raw_data = file.read()
        data = json.loads(raw_data)
        data[level] = {'username': username,
                       'password': password}
        file.seek(0)
        file.write(json.dumps(data, sort_keys=True, indent=4))
        file.truncate()


def get_credentials(level):
    level = str(level)
    with open('credentials.json', 'r', encoding='utf-8') as file:
        raw_data = file.read()
        data = json.loads(raw_data)
        return data[level]
