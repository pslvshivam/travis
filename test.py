from calc import add
from calc import sub
from calc import mult
from calc import div

def test_check_add():
    assert add (3,4) == 7
    
def test_check_wrong_add():
    assert add (8,8) == 7

def test_check_subtract():
    assert sub ( 5 , 1 ) == 4

def test_check_wrong_subtract():
    assert subt( 5 , 4 ) == 3

def test_check_multiply():
    assert mult ( 6,10 ) == 60
    
def test_check_divide():
    assert div ( 12 , 6 ) == 2
