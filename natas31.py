import requests
from natas_utility import *

current_level = 31
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

session = requests.session()

# todo: exploit
files = [('file', ('my_file', b'a,b\n1,2'))]

response = session.post(url, files=files, auth=auth)

# output of HTML table
print(response.content[1458:-98])

# save_credentials(current_level + 1, next_password)
