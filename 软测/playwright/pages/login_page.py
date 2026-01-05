# Playwright Python 的 POM（页面对象）示例
# 位置：软测/playwright/pages/login_page.py
# 依赖：pip install playwright && playwright install

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.profile_selector = "#profile"  # 登录成功后用于断言的元素

    def goto(self):
        self.page.goto(f"{self.base_url}/login")

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_logged_in(self) -> bool:
        return self.page.locator(self.profile_selector).is_visible()
