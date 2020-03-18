from string_calculator import add


def test_empty_string_returns_0():
    assert add('') == 0


def test_string_with_one_number():
    assert add('2') == 2
    assert add('6') == 6
    assert add('58') == 58

def test_string_two_numbers():
    assert add('1,1') == 2
    assert add('8,6') == 14
    assert add('9,3') == 12
