from sys import exit

def buy_the_damn_bike():
    print("Buy the damn bike then!...What color will it be?")

    color = input("> ")

    print("Just kidding, you already won!")
    exit()

def start_question():
    print("Are you going to buy the bike?")

    start_resp = input("> ")
    if "y" in start_resp:
        buy_the_damn_bike()
    else:
        print("Is it too expensive?")

        expensive = input("> ")

        if expensive == "no":
            buy_the_damn_bike()

        elif "y" in expensive:
            print("Can you put a price on happiness?")

###### Put in a loop here to find out a magic price that enables them to buy the buy_the_damn_bike

            happiness = input("> ")

            if happiness == "no":
                buy_the_damn_bike()

            else: partner()

def partner():
    print("Is this about what your partner will say?")

    def alone():
        print("Do you want to die alone happily?")

        happily = input("> ")

        if "y" in happily:
            buy_the_damn_bike()

        else:
            print("Buy a car!")

    def find_partner():
        print("\nOK, do you want to find a partner?")

        find = input("> ")

        if "y" in find:
            buy_the_damn_bike()

        else:
            print("Do you want to die alone?")

            die = input("> ")

            if "y" in die:
                alone()

            if "n" in die:
                find_partner()

    love = input("> ")
    if love == "no":
        buy_the_damn_bike()

    else:
        print("So they want you to be happy?")

        happy = input("> ")

        if "y" in happy:
            buy_the_damn_bike()

        else:
            print("I lied, I'm single")
            find_partner()




#start_question()
partner()
