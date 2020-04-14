
# data
actual_money = 550
actual_water = 400
actual_milk = 540
actual_beans = 120
disponsable_cups = 9

# make coffee function:
def make_coffee(water, milk, beans, price):
    global actual_water, actual_milk, actual_beans, actual_money, disponsable_cups
    actual_water -= water
    actual_milk -= milk
    actual_beans -= beans
    actual_money += price
    disponsable_cups -= 1
    #custom_print(actual_water, actual_milk, actual_beans, disponsable_cups, actual_money)
    
# buy function
def buy(what_):
    global actual_water, actual_milk, actual_beans, actual_money, disponsable_cups
    if what_ == "1":
        if actual_water >= 250 and actual_beans >= 16: 
            make_coffee(250, 0, 16, 4)
            print("I have enough resources, making you a coffee!")
            print("")
    elif what_ == "2":
        if actual_water >= 350 and actual_milk >= 75 and actual_beans >= 20: 
            make_coffee(350, 75, 20, 7)
            print("I have enough resources, making you a coffee!")
            print("")
    elif what_ == "3":
        if actual_water >= 200 and actual_milk >= 100 and actual_beans >= 12:
            make_coffee(200, 100, 12, 6)
            print("I have enough resources, making you a coffee!")
            print("")
        

# fill function
def fill(water_fill, milk_fill, beans_fill, cups_fill):
    global actual_water, actual_milk, actual_beans, actual_money, disponsable_cups
    actual_water += water_fill
    actual_milk += milk_fill
    actual_beans += beans_fill
    disponsable_cups += cups_fill
    #custom_print(actual_water, actual_milk, actual_beans, disponsable_cups, actual_money)

# take function

def take():
    global actual_water, actual_milk, actual_beans, actual_money, disponsable_cups
    print(f"I gave you ${actual_money}")
    actual_money = 0
    #custom_print(actual_water, actual_milk, actual_beans, disponsable_cups, actual_money)
    
    
def custom_print(water, milk, beans, cups, money):
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")
    
def real_print():
    global actual_water, actual_milk, actual_beans, actual_money, disponsable_cups
    print("The coffee machine has:")
    print(f"{actual_water} of water")
    print(f"{actual_milk} of milk")
    print(f"{actual_beans} of coffee beans")
    print(f"{disponsable_cups} of disposable cups")
    print(f"${actual_money} of money")
    print("")

#real_print()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print("")
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        kind_of_coffee = input()
        buy(kind_of_coffee)
    elif action == "fill":
        print("Write how many ml of water do you want to add:")
        water_fill = int(input())
        print("Write how many ml of milk do you want to add:")
        milk_fill = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans_fill = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups_fill = int(input())
        fill(water_fill, milk_fill, beans_fill, cups_fill)  
    elif action == "take":
        take()
    elif action == "remaining":
        real_print()
    elif action == "exit":
        break
    
