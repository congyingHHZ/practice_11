import pytest
def div(a, b):
    return a / b


@pytest.mark.parametrize("in1,in2,out",
                             [(11, 1, 11),
                              (12, 2, 6),
                              (12, 999999, 0.00)
                              ])
def test_div_int(in1, in2, out):
    assert div(in1, in2) == out
    
@pytest.mark.parametrize("in1,in2,out",
                             [(1, 1, 1),
                              (1, 2, 0.5)
                              ])
def test_div_int(in1, in2, out):
    assert div(in1, in2) == out