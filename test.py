from calc import add
from calc import subtract
from calc import multiply
from calc import divide

def test_check_add():
    assert add ( 5 , 2 ) == 7
    
def test_check_wrong_add():
    assert add ( 9 , 4 ) == 7

def test_check_subtract():
    assert subtract ( 5 , 2 ) == 3

def test_check_wrong_subtract():
    assert subtract ( 7 , 2 ) == 3

def test_check_multiply():
    assert multiply ( 5 , 2 ) == 10
    
def test_check_divide():
    assert divide ( 5 , 2 ) == 2.5
