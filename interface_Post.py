import requests

url_LeTiao = "http://www.joysurvey.com:8089/survey/man/user/login"
data_LeTiao = {'phone':'18963988981','password':'123456789A!'}


res = requests.post(url_LeTiao,data_LeTiao)
# 获取响应状态码
print(res.status_code)

# 获取响应信息
print(res.content)

# 获取响应体
print(res.text)

print(res.json())



