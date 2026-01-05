# OWASP ZAP 快速使用指南

## 简介
OWASP ZAP（Zed Attack Proxy）是一个免费的开源安全扫描工具，适合用来做基础的自动化扫描与手动安全测试。

## 快速开始（桌面版）
1. 下载并安装： https://www.zaproxy.org/download/
2. 启动 ZAP，选择“Start with a new session”
3. 在浏览器中设置代理（默认 ZAP 监听 localhost:8080）
4. 浏览应用并让 ZAP 捕获流量
5. 使用 "Quick Start" -> "Automated Scan" 对目标进行快速扫描

## 常见流程
- 被动扫描：对浏览过的流量进行分析（低影响）
- 主动扫描：对发现的入口进行攻击性扫描（可能产生副作用）
- 报告导出：Scan -> Report -> Generate HTML/PDF

## 常见检测项
- SQL 注入（SQLi）
- 跨站脚本（XSS）
- 不安全的 HTTP 标头
- 验证和认证绕过问题
- 敏感信息泄露

## 建议
- 在测试环境或经过授权的测试目标上运行主动扫描
- 结合手工复测和 false-positive 验证
- 将高优先级的发现记录到你的 issue tracker（如 GitHub Issues）

## 使用 CLI（自动化）
ZAP 支持 headless 模式与 API 调用，可在 CI 中集成基本扫描：
示例（以 Docker 方式运行自动化 spider + scanner）：
```
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t https://your-test-site -r zap_report.html
```

## 输出与分析
- 优先处理 High / Medium 风险
- 对每项漏洞记录：复现步骤、影响面、修复建议
