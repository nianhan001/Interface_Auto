import requests


url_LeTiao = "http://www.joysurvey.com:8089/survey/man/user/list?pageNo=1&pageSize=10"
paeams_LeTiao = {'pageNo':'1','pageSize':'10'}

res = requests.get(url=url_LeTiao,params=paeams_LeTiao)

# 获取响应状态码
print(res.status_code)

# 获取响应信息
print(res.content)

# 获取请求头
print(res.request.headers)

# 获取响应体
print(res.text)

print(res.json())