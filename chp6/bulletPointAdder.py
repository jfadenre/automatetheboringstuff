#!python
# adds bullet points to a list of strings
# takes input from clipboard and outputs back to clipboard

import pyperclip

text = pyperclip.paste()
#TODO add code to add *  to beginning of line
lines = text.split('\n')
for i in range(len(lines)): # iterate through all lines
    lines[i] = '* ' + lines[i] #add * to beginning of each line

text = '\n'.join(lines)
pyperclip.copy(text)
