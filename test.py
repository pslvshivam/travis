from calc import add
from calc import substract
from calc import multiply
from calc import divide

def test_check_add():
    assert add (3,4) == 7
    
def test_check_wrong_add():
    assert add (8,8) == 7

def test_check_subtract():
    assert subtract ( 5 , 1 ) == 4

def test_check_wrong_subtract():
    assert subtract ( 5 , 4 ) == 3

def test_check_multiply():
    assert multiply ( 6,10 ) == 60
    
def test_check_divide():
    assert divide ( 12 , 6 ) == 2
