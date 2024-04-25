
fileName = "test_text_file.txt"

def writeToFile(content):
    try:
        with open(fileName, 'a') as file:
            content = content +"\n"
            file.write(content)
            print("content added!")
            file.close()
    except:
        print("An error has occured!")

def readFromFile():
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("An error has occured!")

        

while True:
    print("What would you like to do?")
    print("1: send data   2:read data   3:exit program")
    choice = input("->")
    if choice == "1":
        #Choice 1 writes to the file
        print("What would you like to write to file?")
        content = input("->")
        writeToFile(content)
        print("Content added to file")

    elif choice == "2":
        #choice 2 reads the content of the file
        print("Reading your text file")
        readFromFile()

    elif choice == "3":
        #choice 3 closes the program using 'break' command
        break
print("Good Bye")