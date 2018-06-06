spam = ['cat','bat','rat','elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print('Hello ' + spam[1])
spamLength = len(spam)
print(spamLength)
spamSplice = spam[:3]
print(spamSplice)

print(spam[:])
spam[1] = 'test'
print(spam[:])
