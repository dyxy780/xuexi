# pytest 示例：简单的单元测试（直接运行 pytest 即可）
# 位置：软测/tests/example_unit_test.py

def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

def test_divide_normal():
    assert divide(10, 2) == 5

import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
