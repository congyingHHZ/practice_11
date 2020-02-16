# -*- coding:gbk -*-
import pytest


def div(a, b):
    return a / b


class TestDemo:
    @pytest.mark.parametrize("in1,in2,out",
                             [(10, 5, 2),
                              (999999, 1, 999999),
                              (1, 999999, 0.00),
                              (0, 2, 0)
                              ])
    def test_div_int(self, in1, in2, out):
        assert div(in1, in2) == out

    @pytest.mark.parametrize("in1,in2,out",
                             [(2, 0.01, 200),
                              (10.5, 2, 5.25),
                              (10, 3, 3.33),
                              (0.01, 2, 0.01)
                              ])
    def test_div_float(self, in1, in2, out):
        """
        浮点型，预期结果保留两位小数
        :param in1:除数
        :param in2:被除数
        :param out:预期结果
        :return:
        """
        assert div(in1, in2) == out

    @pytest.mark.parametrize("in1,in2,out",
                             [(-10, 2, -5),
                              (2, -0.01, -200),
                              (-999999, 3, -333333),
                              (-10, -5, 2)
                              ])
    def test_div_negative(self, in1, in2, out):
        assert div(in1, in2) == out

    def test_div_exception(self):
        with pytest.raises(ZeroDivisionError):
            assert div(1, 0)

        with pytest.raises(TypeError):
            assert div('a', 1)

        with pytest.raises(TypeError):
            assert div(1, 'a')
