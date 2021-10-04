from src.bouquet.utility.constants import menu1, flower_list
from src.api_bouquet.api_order import taking_order, checking_order
from src.api_bouquet.pasword import admin_dict, user_dict


def view_menu():
    return menu1


def admin(admin_id, admin_password):
    if admin_id in admin_dict.keys():
        if admin_password == admin_dict[admin_id]:
            return "Access Granted"
        return "Invalid Credentials..."
    else:
        return "Invalid Credentials..."


def user(user_id, user_password):
    if user_id in user_dict.keys():
        if user_password == user_dict[user_id]:
            return "Access Granted"
        return "Invalid Credentials..."
    else:
        return "Invalid Credentials..."


def new_user(new_user_id, new_user_password):
    if new_user_id in user_dict.keys():
        return "User Already Exist..."
    else:
        user_dict[new_user_id] = new_user_password
        return "Registration Successfully..."


def menu_flower_list(menu1):
    for value in menu1.values():
        flower_list.append(value[1])
    return flower_list


def adding_flower(f_code, f_quantity, f_name):
    menu1[f_code] = [f_quantity, f_name]


def deleting_flower(f_code):
    del menu1[f_code]


def ordering(user_bouquet, menu1):
    key, dict_user_bouquet = taking_order(user_bouquet, menu1)
    checking_object = checking_order(key, dict_user_bouquet, menu1)
    return checking_object


def deducting_stock(stock_bouquet):
    key1 = []
    value1 = []
    for i in stock_bouquet:
        if i not in key1:
            key1.append(i)
            value1.append(stock_bouquet.count(i))

    d = dict(zip(key1, value1))
    for i in key1:
        menu1[i][0] = int(menu1[i][0]) - int(d[i])


def all_user_list():
    return user_dict
