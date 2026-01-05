# 软测

此文件夹用于存放软件测试��习相关资料与示例代码（learning/9-week-setup 分支）。

目录结构建议：
- notes/    # 学习笔记（按 week1, week2 ...）
- tests/    # 测试代码（unit, api, ui）
- playwright/# Playwright 自动化（pages, tests）
- k6/       # 性能脚本
- docs/     # 文档（测试计划、报告、指南）

如何运行示例（快速指南）
1. 单元与接口测试（pytest）
   - 安装依赖：
     pip install pytest requests pytest-cov
   - 运行测试并生成 coverage：
     pytest -q --maxfail=1 --junitxml=reports/junit.xml --cov=./ --cov-report=xml

2. Playwright UI 测试
   - 安装 Playwright：
     pip install pytest-playwright playwright
     playwright install
   - 运行 UI 测试：
     pytest softest/playwright/tests -q

3. 性能测试（k6）
   - 安装 k6（https://k6.io）
   - 运行：
     k6 run k6/login_test.js

占位说明
- 所有示例使用了占位 URL 或账号，请在运行前更新环境变量或文件中的 YOUR_APP_BASE_URL / token 等.
