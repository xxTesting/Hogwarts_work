import pytest
import yaml
from python.calc import Calc


class TestCalc:
    @pytest.mark.parametrize("a,b,expected",yaml.load(open(r'../data/adddata.yaml')))
    def test_add(self,a,b,expected):
        self.calc = Calc()
        result = self.calc.add(a, b)
        print(result)
        assert expected == result

    @pytest.mark.parametrize("a,b,expected", yaml.load(open('../data/divdata.yaml')))
    def test_div(self,a,b,expected):
        self.calc = Calc()
        result = self.calc.div(a,b)
        print(result)
        assert expected == result

if __name__ == '__main__':
    pytest.main(['-vs','test_pytest.py::TestCalc::test_div'])
