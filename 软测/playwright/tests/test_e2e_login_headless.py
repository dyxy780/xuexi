"""
Playwright headless E2E test that uses the POM LoginPage.
Location: 软测/playwright/tests/test_e2e_login_headless.py

Requires pytest-playwright and playwright installed.
Run locally: pytest 软测/playwright/tests -k login -q
"""

import os

from ..pages.login_page import LoginPage

BASE_URL = os.getenv("YOUR_APP_BASE_URL", "https://example.com")


def test_e2e_login_headless(page):
    login_page = LoginPage(page, BASE_URL)
    login_page.goto()
    # replace with a real test user if available
    login_page.login("testuser", "password123")
    assert login_page.is_logged_in() is True
