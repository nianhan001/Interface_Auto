# 接口关联操作
import requests
import json

# 先请求登录即可--注意：url一定要和抓包所获取的url一致
url_Login = "http://www.joysurvey.com:8089/survey/man/user/login"
param_LeTiao = {'phone':'18963988981','password':'123456789A!'}

res = requests.post(url=url_Login,data=param_LeTiao)

# 获取响应体数据
print(res.content)

print(res.json())

# 获取登录cookies
# print(res.cookies)


data_Fetch = res.json()['data']
# print(data_Fetch)

token_Fetch = data_Fetch['token']
print(token_Fetch)

# ------------------------------------------------------------

# 第二个接口--修改密码接口

url_Reset = "http://www.joysurvey.com:8089/survey/man/user/resetPassword"
data_ResetPWD = {'id':'15','password1':'123456789A!','password2':'123456789A!'}

headers={
    "token": token_Fetch
}

#以headers形式传给下一个接口
res_002 = requests.post(url=url_Reset,data=data_ResetPWD,headers=headers)

print(res_002.json())

message = res_002.json()['msg']

assert "操作成功000" == message

# --------------------------------------------------------------

# 用户详情接口 /survey/man/user/detail

url_Detail = "http://www.joysurvey.com:8089/survey/man/user/detail"
param_Detail = {'id':'15','username':'LASY','phone':'18888888888','userType':'123456789A!','status':'123456789A'}

headers={
    "token": token_Fetch
}

res_003 = requests.get(url=url_Reset,params=param_Detail,headers=headers)

print(res_003.json())

message = res_003.json()['msg']

assert "操作成功000" == message