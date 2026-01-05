"""
pytest API tests for users and login (data-driven examples)
Location: 软测/tests/api/test_api_users.py
"""

import os
import pytest

BASE_URL = os.getenv("YOUR_APP_BASE_URL", "https://reqres.in")

@pytest.mark.parametrize("page", [1, 2])
def test_get_user_list(session, page):
    url = f"{BASE_URL}/api/users?page={page}"
    resp = session.get(url, timeout=10)
    assert resp.status_code == 200
    body = resp.json()
    assert "data" in body


@pytest.mark.parametrize("email,password,expected_status", [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("invalid@example.com", "wrong", 400),
])
def test_login_variants(session, email, password, expected_status):
    url = f"{BASE_URL}/api/login"
    payload = {"email": email, "password": password}
    resp = session.post(url, json=payload, timeout=10)
    assert resp.status_code == expected_status
    if expected_status == 200:
        body = resp.json()
        assert "token" in body
