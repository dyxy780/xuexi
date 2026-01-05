# 第3周：自动化入门（Pytest）

目标：掌握使用pytest进行自动化测试的基本用法，能够编写并运行简单自动化用例。

每天安排（每天约2小时）：

- 周一：Python与pytest准备
  - 安装Python、pip与虚拟环境（venv）。
  - 安装pytest并运行示例用例（pytest -q）。

- 周二：pytest基础语法
  - 学习用例函数命名、断言、setup/teardown思想。
  - 编写若干简单测试函数并实践断言用法。

- 周三：fixture与参数化
  - 理解fixture的作用范围（function/module/session）并编写示例。
  - 学习参数化（@pytest.mark.parametrize）并实现数据驱动测试。

- 周四：组织测试与目录结构
  - 规范化测试项目目录结构（tests/、conftest.py、测试数据目录）。
  - 将已有手动用例转化为自动化脚本的示例。

- 周五：运行与报告
  - 学习pytest命令行选项、用例选择与跳过标记（skip、xfail）。
  - 集成生成简单的测试报告（如--junitxml或第三方插件）。

- 周六：实战：API或函数级自动化
  - 选择一个简单接口或函数，编写完整的自动化测试用例并运行。

- 周日：复盘与代码质量
  - 整理本周代码，添加注释与README。
  - 学习如何在CI中运行pytest（概念）。

检查点：能用pytest构建基本自动化测试框架并稳定执行测试套件。