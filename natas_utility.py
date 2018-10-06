import json


def save_credentials(level, password):
    username = 'natas{}'.format(level)
    if level is not str:
        level = str(level)
    with open('credentials.json', 'r+', encoding='utf-8') as file:
        raw_data = file.read()
        data = json.loads(raw_data)
        data[level] = {'username': username,
                       'password': password}
        file.seek(0)
        file.write(json.dumps(data, sort_keys=True, indent=4))
        file.truncate()


def get_credentials(level):
    if level is not str:
        level = str(level)
    with open('credentials.json', 'r', encoding='utf-8') as file:
        raw_data = file.read()
        data = json.loads(raw_data)
        return data[level]
