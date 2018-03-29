import sys, os
sys.path.append(os.path.abspath('../mahjong'))
from calculator import calculator

def test_str9_to_array34(cal):
    return cal.str9_to_array34(man='111', sou='11178999', honor='222')


if __name__ == '__main__':
    cal = calculator()
    str = test_str9_to_array34(cal)
    cal.agari(str)
    