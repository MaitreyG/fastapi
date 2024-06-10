import pytest
from app.calculations import add,subtract,multiply,divide

@pytest.mark.parametrize("num1,num2,expected",[
  (3,2,5),
  (7,1,8),
  (12,4,16)
])
def test_add(num1,num2 ,expected):
  sum=add(num1,num2)
  assert sum==expected

def test_subtract():
  assert subtract(9,4) == 5