# 接口自动化测试练习项目

使用 Python、Pytest、Requests 和 YAML 实现本地登录接口的数据驱动测试，支持 Allure 测试结果输出。

## 安装依赖

在项目目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## 运行

第一个终端启动本地模拟接口：

```powershell
.\.venv\Scripts\python mock_server.py
```

第二个终端在项目目录执行测试：

```powershell
.\.venv\Scripts\python -m pytest --alluredir=allure-results
```

如果已单独安装 Allure 命令行工具，可以执行 `allure serve allure-results` 查看报告。

## 项目结构

- `mock_server.py`：本地 Flask 登录接口，监听 127.0.0.1:8787。
- `testcases/login/`：登录测试和 YAML 数据。
- `utils/`：HTTP 请求与 YAML 读取封装。
- `pytest.ini`：测试发现和失败重跑配置。

模拟接口中的 admin / 123456 和 abc123 均为练习用示例数据。当前三个参数化测试仅断言 HTTP 状态码为 200；业务响应断言可后续完善。login.yaml 是另一种数据格式的练习文件，目前未被测试加载。本项目不包含 Redis 或 Jenkins 配置。

虚拟环境、缓存、Allure 输出、IDE 配置及环境变量文件均通过 .gitignore 排除。
