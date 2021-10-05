import pytest

from src.api_bouquet.agent import *
from src.bouquet.utility.constants import menu1


def test_view_menu():
    output = view_menu()
    assert output == menu1


@pytest.mark.parametrize('admin_id, admin_password, result', [
    ('Abhishek', 'Abhishek', 'Access Granted'),
    ('Prabhat', 'Prabhat', 'Invalid Credentials...'),
    ('Abhi', 'Abhi', 'Invalid Credentials...'),
    ('Abhishek', 'Anand', 'Invalid Credentials...'),
    ('', '', 'Invalid Credentials...'),
    ('Abhishek', '', 'Invalid Credentials...'),
    ('', 'Rohit', 'Invalid Credentials...')
])
def test_admin(admin_id, admin_password, result):
    output = admin(admin_id, admin_password)
    assert output == result


@pytest.mark.parametrize('user_id, user_password, result', [
    ('Abhishek', 'Abhishek', 'Access Granted'),
    ('Prabhat', 'Prabhat', 'Access Granted'),
    ('Abhi', 'Abhi', 'Access Granted'),
    ('Anand', 'Prabhat', 'Invalid Credentials...'),
    ('', '', 'Invalid Credentials...'),
    ('Abhishek', '', 'Invalid Credentials...'),
    ('', 'Rohit', 'Invalid Credentials...')
])
def test_user(user_id, user_password, result):
    output = user(user_id, user_password)
    assert output == result


@pytest.mark.parametrize('new_user_id, new_user_password, result', [
    ('Abhishek', 'Abhishek', 'User Already Exist...'),
    ('Prabhat', 'Prabhat', 'User Already Exist...'),
    ('Abhi', 'Abhi', 'User Already Exist...'),
    ('Anand', 'Prabhat', 'Registration Successfully...'),
    ('', '', 'Invalid Credentials...'),
    ('Abhishek', '', 'Invalid Credentials...'),
    ('', 'Rohit', 'Invalid Credentials...')
])
def test_new_user(new_user_id, new_user_password, result):
    output = new_user(new_user_id, new_user_password)
    assert output == result


@pytest.mark.parametrize('menu1, flower_list', [
    (menu1, ['Rose', 'Lily', 'Tulip', 'Daisy', 'Orchid']),
])
def test_menu_flower_list(menu1, flower_list):
    output = menu_flower_list(menu1)
    assert output == flower_list


@pytest.mark.parametrize('user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu', [
    ('ABCDE', menu1, [], 'ABCDE', []),
    ('SGFGGT', menu1, ['S', 'G', 'F', 'T'], '', []),
    ('ABBBBBDEV', menu1, ['V'], 'ABBBBBDE', []),
    ('', menu1, [], '', []),
    ('AAAAAAACXDEAQ', menu1, ['X', 'Q'], 'AAAAACDE', ['A']),
    ('AAAAAAABBBBBBBBSSSSXXXDDDDDDDDDDQQQZXX', menu1, ['S', 'X', 'Q', 'Z'], 'AAAAABBBBBDDDDD', ['A', 'B', 'D']),
])
def test_ordering(user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu):
    output = ordering(user_bouquet, menu1)
    assert output == (not_in_menu, stock_bouquet, overflow_menu)


@pytest.mark.parametrize('result', [
    ({'Abhishek': 'Abhishek', 'Abhi': 'Abhi', 'Prabhat': 'Prabhat'})
])
def test_all_user_list(result):
    output = all_user_list()
    assert output == result
