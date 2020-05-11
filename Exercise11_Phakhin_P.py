number = int(input("Number: "))
space = number
for i in range(number):
    space = space - 1
    text = ""
    for p in range(2*i+1):
        text += "*"
    print(" "*space+text)