import pytest

class demo():
    def plus(self,a,b):
        result=a+b
        return result
    def test_demo(self):
        assert demo().plus(1,3)==4

if __name__ == '__main__':
        pytest.main()
