from main import mean
import pytest

@pytest.mark.parametrize("a,b",[([1, 2, 3, 4, 5],3),
                                ([1, 10, 3, 4, 5],5),
                                ([1, 2, 12, 4, 4],4.6)])
def test_is_correct(a,b):
   assert mean(a) == b

def test_zero_correct():
   with pytest.raises():
    mean()

@pytest.mark.parametrize("c,d",[(TypeError,3),
                                (TypeError,"a")
                              ])
def test_error(c,d):
   with pytest.raises(c):
    mean(d)
