import pytest as pytest
from src.api_bouquet.api_order import taking_order, checking_order
from src.bouquet.utility.constants import menu1


@pytest.mark.parametrize('user_bouquet, menu1, key, dict_user_bouquet', [
    ('ABC', menu1, ['A', 'B', 'C'], {'A': 1, 'B': 1, 'C': 1}),
    ('ABCDE', menu1, ['A', 'B', 'C', 'D', 'E'], {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}),
    ('AAABBCE', menu1, ['A', 'B', 'C', 'E'], {'A': 3, 'B': 2, 'C': 1, 'E': 1}),
    ('', menu1, [], {}),
    ('QWERSD', menu1, ['Q', 'W', 'E', 'R', 'S', 'D'], {'Q': 1, 'W': 1, 'E': 1, 'R': 1, 'S': 1, 'D': 1}),
    ('', '', [], {})
])
def test_taking_order(user_bouquet, menu1, key, dict_user_bouquet):
    output = taking_order(user_bouquet, menu1)
    assert output == (key, dict_user_bouquet)


@pytest.mark.parametrize('key, dict_user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu', [
    (['A', 'B', 'C'], {'A': 1, 'B': 1, 'C': 1}, menu1, [], 'ABC', []),
    (['A', 'B', 'C', 'D', 'E'], {'A': 5, 'B': 2, 'C': 1, 'D': 3, 'E': 1}, menu1, [], 'AAAAABBCDDDE', []),
    ([], {}, menu1, [], '', []),
    (['C', 'Z', 'N', 'Q', 'E'], {'C': 1, 'Z': 1, 'N': 1, 'Q': 1, 'E': 1}, menu1, ['Z', 'N', 'Q'], 'CE', []),
    (['X', 'W', 'P', 'U'], {'X': 4, 'W': 2, 'P': 1, 'U': 1}, menu1, ['X', 'W', 'P', 'U'], '', []),
    (['X', 'W', 'A', 'B', 'E', 'C'], {'X': 4, 'W': 2, 'A': 7, 'B': 1, 'E': 10, 'C': 4}, menu1, ['X', 'W'], 'AAAAABEEEEECCCC', ['A', 'E']),
])
def test_checking_order(key, dict_user_bouquet, menu1, not_in_menu, stock_bouquet, overflow_menu):
    output = checking_order(key, dict_user_bouquet, menu1)
    assert output == (not_in_menu, stock_bouquet, overflow_menu)
