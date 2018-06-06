while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Please enter an age.")

while True:
    print("Enter your name:")
    name = input()
    if name.isalpha():
        break
    print("Please enter a name.")

print(name + " is " + age + " years old")
