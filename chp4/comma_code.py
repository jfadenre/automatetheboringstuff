spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(listName):
    commaCode = []
    for i in range((len(listName))):
        if i == (len(listName)-1):
            commaCode.append('and ' + listName[i])
            #print('and ' + listName[i])
        else:
            commaCode.append(listName[i] + ', ')
            #print(listName[i] + ', ')
    output = ''
    for i in range((len(commaCode))):
        output += commaCode[i]
    print(output)


comma(spam)
