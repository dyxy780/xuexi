"""
conftest.py - pytest 全局配置与常用fixture示例

说明：
- 该文件提供常用的fixture示例（requests session、配置读取、样例数据）。
- 根据项目实际情况调整并扩展fixture。
"""

import os
import pytest
import requests


@pytest.fixture(scope="session")
def config():
    """读取测试配置（示例：可从环境变量或配置文件读取）"""
    return {
        "base_url": os.environ.get("BASE_URL", "https://example.com/api"),
        "auth_token": os.environ.get("AUTH_TOKEN", "")
    }


@pytest.fixture(scope="session")
def session(config):
    """requests.Session的简单封装，自动注入鉴权头"""
    s = requests.Session()
    token = config.get("auth_token")
    if token:
        s.headers.update({"Authorization": f"Bearer {token}"})
    s.headers.update({"Accept": "application/json"})
    yield s
    s.close()


@pytest.fixture
def sample_data():
    """返回示例测试数据"""
    return {
        "user": {"username": "test_user", "password": "pass123"},
        "item": {"name": "sample", "value": 1}
    }


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="测试环境：dev/staging/prod")


@pytest.fixture
def env(request):
    return request.config.getoption("--env")
