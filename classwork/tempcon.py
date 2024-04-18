#Github Example
#This code should be downloaded from Github and copied into your VS Code
#Save it in your "classwork" folder with the name "gitHubExample.py"

#Complete the following code using your resources

######################################################

#Temperature Converter
#This program converts temperatures between Fahrenheit and Celcius

#It allow the user to specify if which way they want to convert
#The user then inputs their temperature
#And the converted number is printed to the terminal


print("Temperature Converter")
print("Which converstion would you like: (1) F to C, (2) C to F")
user_choice = input("->")
if user_choice == "1":
    print("Converting F to C")
    print("What is your number?")
    temp_input = input("->")
    #conversion: °C = (°F - 32) × 5/9
    temp_output = (float(temp_input)-32)*(5/9)
    print(temp_output," C")
elif user_choice == "2":
    print("Converting C to F")
    print("What is your number?")
    temp_input = input("->")
    #conversion °F = (°C × (9/5)) + 32
    temp_output= (float(temp_input)*(9/5))+32
    print(temp_output,"C")
else:
    print("error")
