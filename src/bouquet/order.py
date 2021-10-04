from src.bouquet.utility.constants import menu1, history
from src.bouquet.utility.printing import *
from src.bouquet.stock_maintain import *
from src.bouquet.utility.date_time import date_time


def gateway():  # 2nd most important function after main func, called gateway
    print("---- Welcome To Flower Shop ----")
    while True:
        choose_menu()
        n = input("Enter choice : ")
        separate_line()

        if n == "1":
            display_menu(menu1)
            separate_line()

        elif n == "2":
            o2 = FlowerInventory()
            o2.add_flower(menu1)
            separate_line()

        elif n == "3":
            o2 = FlowerInventory()
            o2.del_flower(menu1)
            separate_line()

        elif n == "4":
            matching_order_and_user_bouquet()
            separate_line()

        elif n == "5":
            display_order_history(history)
            separate_line()

        elif n == "6":
            thanks_for_visiting()
            break

        else:
            invalid_input()
            separate_line()


# In this order module there are one purchase function which is main gateway for processing of order
# 1--> taking order, 2--> checking_order, 3--> checking_stock, 4--> order_confirmation
# All four function is going to execute one after one as the next function is called by the previous function

def matching_order_and_user_bouquet():
    while True:
        bouquet_size = input("Enter Bouquet Size : ")
        user_bouquet = input("Enter Bouquet : ").upper()

        if len(user_bouquet) == int(bouquet_size) and len(user_bouquet) != 0:
            taking_order(user_bouquet)
            break
        else:
            print("Entered Bouquet is NOT equal to Bouquet size...")
            separate_line()


def taking_order(user_bouquet):
    key = []
    value = []

    print("Your Ordered Bouquet : ", user_bouquet, '\n')

    for i in user_bouquet:  # counting the occurrence of a particular flower e.g A=2, B=1, C=2, D=1
        if i not in key:
            key.append(i)
            value.append(user_bouquet.count(i))
    dict_user_bouquet = dict(zip(key, value))  # converting that user_bouquet into dictionary
    checking_order(key, dict_user_bouquet)  # calling next function
    return key, dict_user_bouquet


def checking_order(key, dict_user_bouquet):
    flag = 0  # flag and count both used for switching b/w condition
    count = 0
    not_in_menu1 = []  # empty list which store that flower which is not present in menu
    stock_bouquet = ''  # empty string which stores the flower which is available in stock from user_bouquet
    for i in key:
        if i not in menu1.keys():
            not_in_menu1.append(i)
            count += 1
            # count != 0 --> all flowers are not present in menu...and adding unavailable flowers in "not_in_menu" list
        else:
            if int(dict_user_bouquet[i]) <= int(menu1[i][0]):
                stock_bouquet = stock_bouquet + (i * dict_user_bouquet[i])
                # here count == 0 & flag ==  0 --> means all flowers of user bouquet is available in stock...
            else:
                print("Sorry {} is only {} in stock...".format(i, menu1[i][0]))
                stock_bouquet = stock_bouquet + (i * menu1[i][0])
                flag += 1
    checking_stock(count, not_in_menu1, stock_bouquet)  # calling next function
    order_confirmation(flag, stock_bouquet)
    return count, not_in_menu1, stock_bouquet, flag


def checking_stock(count, not_in_menu1, stock_bouquet):
    # this function prints both -->  not present in menu(not-in_menu) & available in stock(stock_bouquet)
    if count != 0:
        print("Sorry😥...{} is not in our Menu...".format(not_in_menu1))
        print("Flowers currently In stock : ", stock_bouquet, '😃\n')


def order_confirmation(flag, stock_bouquet):
    if flag == 0:
        show_option()
        choice_input(stock_bouquet)

    else:
        show_option()
        choice_input(stock_bouquet)


# this choice_input is a function which is in infinite loop till the user didn't enter the desirable input..
# if user enters correct input then, it will proceed further...

def choice_input(stock_bouquet):
    while True:
        n = input("Enter choice --> : ")
        separate_line()
        if n == "1":
            congratulation()
            print("Placed Order : ", stock_bouquet)
            date_time()
            o2 = FlowerInventory()
            o2.deducting_from_stock(menu1, stock_bouquet)  # deducting quantity from database
            break

        elif n == "2":
            display_menu(menu1)  # showing menu
            matching_order_and_user_bouquet()
            break

        elif n == "0":
            visit_again()
            break

        else:
            print("Invalid..Input")
            separate_line()
