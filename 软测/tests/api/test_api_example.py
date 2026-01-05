# pytest + requests 的接口测试示例
# 位置：软测/tests/api/test_api_example.py
# 运行前：pip install requests pytest

import os
import requests

BASE_URL = os.getenv("YOUR_APP_BASE_URL", "https://reqres.in")  # 占位，替换为实际地址

def test_get_user_list():
    resp = requests.get(f"{BASE_URL}/api/users?page=2", timeout=10)
    assert resp.status_code == 200
    body = resp.json()
    assert "data" in body

def test_login_success():
    # 以 reqres.in 为例的登录模拟接口
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    resp = requests.post(f"{BASE_URL}/api/login", json=payload, timeout=10)
    assert resp.status_code == 200
    body = resp.json()
    assert "token" in body

def test_login_invalid_credentials():
    payload = {"email": "invalid@example.com", "password": "wrong"}
    resp = requests.post(f"{BASE_URL}/api/login", json=payload, timeout=10)
    assert resp.status_code == 400  # reqres 返回 400 表示错误
