# Playwright E2E 测试示例（pytest + playwright）
# 位置：软测/playwright/tests/test_e2e_login.py
# 运行前：pip install pytest-playwright playwright && playwright install
# 说明：此示例使用 pytest-playwright 提供的 page fixture

import os
import pytest

# 以下为相对导入示例（如果项目结构如示例）
from ..pages.login_page import LoginPage  # path: soft_test/playwright/pages/login_page.py

BASE_URL = os.getenv("YOUR_APP_BASE_URL", "https://example.com")  # 占位

def test_e2e_login(page):
    login_page = LoginPage(page, BASE_URL)
    login_page.goto()
    # 使用占位用户名/密码，替换为真实测试账号
    login_page.login("testuser", "password123")
    # 等待并断言登录后的页面状态（示例）
    assert login_page.is_logged_in() is True
