import os
import re
import subprocess

files = [file for file in os.listdir('.') if 'natas' in file and 'utility' not in file]

files = sorted(files, key=lambda x: int(re.findall(r'(\d+)\.py$', x)[0]))

for file in files:
    print(file, subprocess.check_output(['py', file]).decode('utf-8'), end='')
