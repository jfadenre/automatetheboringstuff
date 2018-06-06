#!python
# pw.py an insecure password manager
# 5/29/2018

PASSWORD = {'email': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
            'blog': 'def53e95f1fc7a2aa7dbc4685f282f1e3e4ea3b364b07622e58edb15d239b252',
            'luggage': '12345'}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('Usage: pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print("copying account: " + account + " to clipboard")
else:
    print('There is no account ' + account)

