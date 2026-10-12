#无敌整合
from utils.new_yamlutil import YamlReader
from utils.APIRequest import APIRequest


class APIUtil:

    #通过类名调用，不用先创建 APIUtil 对象
    @staticmethod
    #读取 YAML，然后把请求需要的信息取出来。
    def get_case_info(yaml_file):
        case_info = YamlReader(yaml_file).data()

        url = str(case_info[0]['request']['url'])
        method = case_info[0]['request']['method']
        headers = case_info[0]['request']['headers']
        data = case_info[0]['request']['data']

        return url, method, headers, data

    @staticmethod
    def send_request(yaml_file):
        url, method, headers, data = APIUtil.get_case_info(yaml_file)

        req = APIRequest()
        #发送请求，并且把 response 返回出去
        return req.send_request(
            url=url,
            data=data,
            headers=headers,
            method=method
        )