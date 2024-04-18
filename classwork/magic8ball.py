import random
random_number = random.randint(1,8)
print("------------------------------------------")
print("|Welcom To Magic 8 Ball                   |")
input("|Ask Magic 8 Ball your question -> ")
print("|your magic statement is                  |")

if random_number == 1:
    print("|[Yes]                                    |")
elif random_number == 2:
    print("|[no]                                     |")
elif random_number == 3:
    print("|[Ask again later]                        |")
elif random_number == 4:
    print("|[My sources say no]                      |")
elif random_number == 5:
    print("|[Very doubtful]                          |")
elif random_number == 6:
    print("|[It is certain]                          |")
elif random_number == 7:
    print("|[Most likely]                            |")
elif random_number == 8:
    print("|[My sources say no]                      |")
else:
    print("HOW")
print("------------------------------------------")