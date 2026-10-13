from utils.APIUtil import APIUtil
import pytest

@pytest.fixture
def prepare_test():
    print("测试开始前：准备测试环境")
    common_data = {
        "expected_status_code": 200
    }
    yield common_data

    print("测试结束后：清理测试环境")


#把下面的 test_login() 执行 3 次，每次传进去一个不同的 YAML 文件。
@pytest.mark.parametrize("yaml_file", [
    'testcases/login/login_success.yaml',
    'testcases/login/login_fail_wrong_password.yaml',
    'testcases/login/login_fail_invalid_user.yaml'
])
def test_login(yaml_file,prepare_test):
    res = APIUtil.send_request(yaml_file)

    #assert res.json()['message'] == '登录成功'
    #前面断言通过才会执行后面的

    #HTTP 状态码 200 表示这次 HTTP 请求成功被服务器正常处理了
    assert res.status_code == prepare_test["expected_status_code"]

#改一下
#python mock_server.py  flask模拟登录接口服务器
#$env:PYTHONPATH = "."  告诉 Python：当前 myxiangmu 目录也要作为导包的查找位置。
#python -m pytest        --alluredir=allure-results    生成Allure 报告