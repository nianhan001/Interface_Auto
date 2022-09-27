import requests
import json

url_Login = "http://www.joysurvey.com:8089/survey/man/user/login"
param_LeTiao = {'phone':'18963988981','password':'123456789A!'}

res = requests.post(url=url_Login,data=param_LeTiao)

# 打印状态码
print(res.status_code)

# 打印响应数据
print(res.json())

message = res.json()['msg']

# assert a = b
assert "操作成功" == message

assert "0000" == res.json()['code']

