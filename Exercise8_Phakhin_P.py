usernameInput = input("username: ")
passwordInput = input("password: ")
if usernameInput == "Phakhin" and passwordInput == "1943":
    print("Welcome to the shop")
    print("--------------------")
    print("  Products     price")
    print("1. apple        40")
    print("2. banana       10")
    print("3. pineapple    30")
    print("4. mango        50")
    print("--------------------")
    chooseInput = int(input("choose number: "))
    pieceInput = int(input("how many: "))
    print("Total")
    if chooseInput == 1:
        print(str(40 * pieceInput))
    elif chooseInput == 2:
        print(str(10 * pieceInput))
    elif chooseInput == 3:
        print(str(30 * pieceInput))
    elif chooseInput == 4:
        print(str(50 * pieceInput))
    print("--------------------")
    print("Thank you")
else:
    print("Wrong username or password")
