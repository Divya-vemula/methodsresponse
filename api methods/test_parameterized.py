import pytest
import parameterized

test_data=[[1,2,3],
           [2,4,8],
           [3,3,9]]

@pytest.mark.parametrize("a,b,e",test_data)
def test_mul(a,b,e):
    assert a*b == e


