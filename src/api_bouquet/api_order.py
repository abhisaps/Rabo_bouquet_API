def taking_order(user_bouquet, menu1):
    key = []
    value = []
    for i in user_bouquet:
        if i not in key:
            key.append(i)
            value.append(user_bouquet.count(i))
    dict_user_bouquet = dict(zip(key, value))
    checking_order(key, dict_user_bouquet, menu1)
    return key, dict_user_bouquet


def checking_order(key, dict_user_bouquet, menu1):
    stock_bouquet = ''
    not_in_menu1 = []
    overflow_menu = []
    for i in key:
        if i not in menu1.keys():
            not_in_menu1.append(i)
        else:
            if int(dict_user_bouquet[i]) <= int(menu1[i][0]):
                stock_bouquet = stock_bouquet + (i * dict_user_bouquet[i])
            else:
                overflow_menu.append(i)
                if menu1[i][0] != 0:
                    stock_bouquet = stock_bouquet + (i * menu1[i][0])

    return not_in_menu1, stock_bouquet, overflow_menu

