#APIUtil整合包
#APIRequest 类，负责发送请求
import requests
#后面调用api_request = APIRequest()创建 APIRequest 对象
class APIRequest:
    def __init__(self):
        #什么都不做，暂时不用初始化任何东西
        pass
        print('准备执行')


    def send_request(self,method, url, data=None, headers=None):
        try:
            response = requests.request(
                method=method,
                url=url,
                data=data,
                headers=headers,
                verify=False,

            )
            return response
    #出现异常as e：把具体的异常信息保存到变量 e 中。
        except Exception as e:
            print(f'请求出错:{e}')
            return None

