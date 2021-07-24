from data import MENU, resources

loop = True
money = 0


def customer(customer_option):
    menu = MENU[customer_option]
    inger = menu["ingredients"]
    return inger


def customer_cost(customer_option_cost):
    cost = MENU[customer_option_cost]
    cost_of = cost["cost"]
    return cost_of


def coin(quarters, dimes, nickles, pennies):
    no_of_quarters = quarters * 0.25
    no_of_dimes = dimes * 0.10
    no_of_nickles = nickles * 0.05
    no_of_pennies = pennies * 0.01
    sums = no_of_quarters + no_of_dimes + no_of_nickles + no_of_pennies
    return sums.__round__(2)


def product():
    for item in customer(option):
        resources[item] -= customer(option)[item]


def compare():
    for items in customer(option):
        if resources[items] < customer(option)[items]:
            print(f"sorry out of {items}")
            return False
        else:
            return True


while loop:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == "espresso" or option == "latte" or option == "cappuccino":
        if compare():
            product()
            print("please insert coins")
            coin1 = int(input("how many quarters?: "))
            coin2 = int(input("how many dimes?: "))
            coin3 = int(input("how many nickles?: "))
            coin4 = int(input("how many pennies?: "))
            coin(coin1, coin2, coin3, coin4)
            if coin(coin1, coin2, coin3, coin4) == customer_cost(option):
                print(f"here is your {option} coffee ☕. Enjoy!")
                money += customer_cost(option)
            elif coin(coin1, coin2, coin3, coin4) > customer_cost(option):
                balance = coin(coin1, coin2, coin3, coin4) - customer_cost(option)
                print(f"here is {balance.__round__(2)}$ in change\nhere is your {option} coffee ☕. Enjoy!")
                money += customer_cost(option)
            else:
                print("Sorry that's not enough money. Money refunded🥺")
    elif option == "off":
        loop = False
    elif option == "report":
        print(
            f"water : {resources['water']}ml\nmilk : {resources['milk']}ml\ncoffee : {resources['coffee']}g\nMoney : {money}$")
    else:
        print("please enter right option")
