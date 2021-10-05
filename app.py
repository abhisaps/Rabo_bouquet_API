from flask import Flask, render_template, request
from src.api_bouquet.agent import *
from src.bouquet.utility.constants import menu1


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("welcome.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')


@app.route('/admin_confirmation', methods=['POST', 'GET'])
def admin_confirmation():
    output = request.form.to_dict()
    admin_id = output['admin_id']
    admin_password = output['admin_password']
    msg = admin(admin_id, admin_password)

    if msg == "Access Granted":
        return render_template('admin_home.html')
    else:
        return render_template('/admin_login.html', msg=msg)


@app.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')


@app.route('/admin_display_menu')
def admin_display_menu():
    output = view_menu()
    return render_template('admin_display_menu.html', output=output)


@app.route('/add_flower')
def add_flower():
    return render_template('admin_add_flower.html')


@app.route('/add_confirmation', methods=['POST', 'GET'])
def add_confirmation():
    output = request.form.to_dict()
    f_code = output['f_code'].upper()
    f_quantity = output['f_quantity']
    f_name = output['f_name'].capitalize()

    f_list = menu_flower_list(menu1)

    if f_code.isalpha() and f_quantity.isdigit() and f_name.isalpha():
        if 200 > int(f_quantity) > 0:
            if f_name not in f_list:
                adding_flower(f_code, f_quantity, f_name)
                return render_template('admin_add_flower.html', f_code=f_code)
            else:
                return render_template('admin_add_flower.html', msg="FLower name should be unique...")
        else:
            return render_template('admin_add_flower.html', msg="Quantity must be greater than zero & less than 200")
    else:
        return render_template('admin_add_flower.html', msg="Invalid input...")


@app.route('/del_flower')
def del_flower():
    return render_template('admin_del_flower.html')


@app.route('/del_confirmation', methods=['POST', 'GET'])
def del_confirmation():
    output = request.form.to_dict()
    f_code = output['f_code'].upper()

    if f_code in menu1:
        deleting_flower(f_code)
        return render_template('admin_del_flower.html', f_code=f_code)
    else:
        return render_template('admin_del_flower.html', msg="Please input Correct Flower...")


@app.route('/user_list')
def user_list():
    output = all_user_list()
    return render_template('admin_user_list.html', output=output)


@app.route('/records')
def records():
    return render_template('admin_records.html')


@app.route('/user_login')
def user_login():
    return render_template('user_login.html')


@app.route('/user_confirmation', methods=['POST', 'GET'])
def user_confirmation():
    output = request.form.to_dict()
    user_id = output['user_id']
    user_password = output['user_password']
    msg = user(user_id, user_password)

    if msg == "Access Granted":
        return render_template("user_home.html", user_id=user_id)
    else:
        return render_template('/user_login.html', msg=msg)


@app.route('/new_user_registration')
def new_user_registration():
    return render_template('new_user_registration.html')


@app.route('/new_user_confirmation', methods=['POST', 'GET'])
def new_user_confirmation():
    output = request.form.to_dict()
    new_user_id = output['new_user_id']
    new_user_password = output['new_user_password']

    msg = new_user(new_user_id, new_user_password)

    if msg == "User Already Exist...":
        return render_template('new_user_registration.html', msg=msg)
    elif msg == "Invalid Credentials...":
        return render_template('new_user_registration.html', msg='Id and Password can not be empty')
    else:
        return render_template('new_user_registration.html', msg1=msg)


@app.route('/user_home')
def user_home():
    return render_template('user_home.html')


@app.route('/user_display_menu')
def user_display_menu():
    output = view_menu()
    return render_template("user_display_menu.html", output=output)


@app.route('/user_bouquet_size_confirmation', methods=['POST', 'GET'])
def user_bouquet_size_confirmation():
    bouquet_size = request.form['bouquet_size']
    output = view_menu()
    if bouquet_size.isdigit() and int(bouquet_size) > 0:
        return render_template('user_display_menu.html', bouquet_size=bouquet_size, output=output)
    else:
        return render_template('user_display_menu.html', msg1="Invalid Input...Select Bouquet size", output=output)


@app.route('/user_order_confirmation', methods=['POST', 'GET'])
def user_order_confirmation():
    output = request.form.to_dict()
    user_bouquet = output['user_bouquet'].upper()
    bouquet_size = output['bouquet_size']
    output = view_menu()

    o1 = ordering(user_bouquet, menu1)
    not_in_menu = list(o1)[0]
    stock_bouquet = list(o1)[1]
    overflow_menu = list(o1)[2]

    if user_bouquet.isalpha() and len(user_bouquet) != 0:
        if len(user_bouquet) < int(bouquet_size):
            return render_template('user_display_menu.html', user_bouquet=user_bouquet, not_in_menu=not_in_menu, stock_bouquet=stock_bouquet, len_stock_bouquet=len(stock_bouquet), overflow_menu=overflow_menu, output=output, bouquet_size=bouquet_size)
        else:
            if not_in_menu == [] and overflow_menu == []:
                deducting_stock(stock_bouquet)
                return render_template('receipt.html', msg3='Your Order has been Placed Successfully...', stock_bouquet=stock_bouquet)
            else:
                return render_template('user_display_menu.html', user_bouquet=user_bouquet, not_in_menu=not_in_menu, stock_bouquet=stock_bouquet, len_stock_bouquet=len(stock_bouquet), overflow_menu=overflow_menu, output=output, bouquet_size=bouquet_size, user_bouquet_size=len(user_bouquet))
    else:
        return render_template('user_display_menu.html', output=output, msg2='User Bouquet can\'t be empty', user_bouquet=user_bouquet, bouquet_size=bouquet_size)


if __name__ == "__main__":
    app.run(debug=True)
