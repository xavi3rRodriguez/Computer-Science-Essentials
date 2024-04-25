filename = "User_name.txt"

def writeToFile(content):
    try:
        with open(filename, "a") as file:
            content = content + "\n"
            file.write(content)
            print("name added")
            file.close()
    except:
        print("error")

def readFromFile():
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("error")

while True:
    print("what do you want to do")
    print("1: add name   2:read names   3:leave")
    choice = input("->")

    if choice == "1":
        print("What name would you like to add?")
        content = input("->")
        writeToFile(content)
        print("added name to file")

    elif choice == "2":
        print("printing names")
        readFromFile()

    elif choice == "3":
        break
print("you leave NOW")