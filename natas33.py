import requests
from natas_utility import *

current_level = 33
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

session = requests.session()

response = session.get(url, auth=auth)

content = response.content.decode('utf-8')

# Congratulations! You have reached the end... for now.
print(content[794:-24])
