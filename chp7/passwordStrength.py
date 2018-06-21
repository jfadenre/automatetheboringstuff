#!python3

import re

print('Enter password to check for compliance: ')
password = input()



lengthCheck = re.compile(r'(\w{8,})+')
upperCaseCheck = re.compile(r'[A-Z]+')
lowerCaseCheck = re.compile(r'[a-z]+')
digitCheck = re.compile(r'\d+')

def checkPass(passwordCheck):
    lengthPass = False
    upperCasePass = False
    lowerCasePass = False
    digitPass = False

    if lengthCheck.search(passwordCheck):
        lengthPass = True

    if upperCaseCheck.search(passwordCheck):
        upperCasePass = True
    
    if lowerCaseCheck.search(passwordCheck):
        lowerCasePass = True

    if digitCheck.search(passwordCheck):
        digitPass = True

    if lengthPass and upperCasePass and lowerCasePass and digitPass:
        return True
    else:
        return False


if checkPass(password):
    print('Password is compliant')
else:
    print('Password is not compliant')
