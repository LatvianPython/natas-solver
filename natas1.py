import requests
import re
from natas_utility import *

current_level = 1
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

response = session.get(base_url, auth=auth)

content = response.content.decode('utf-8')

password_regex = re.compile(r'<!--The password for natas2 is (.+) -->')
next_password = password_regex.findall(content)[0]
print(next_password)

if next_password is not None:
    save_credentials(current_level + 1, next_password)
