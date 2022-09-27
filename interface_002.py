import requests
import json


url_LeTiao = "http://www.joysurvey.com:8089/survey/man/user/login"
data_LeTiao = {'phone':'18963988981','password':'123456789A!'}

#访问登录接口，并获取token。

res = requests.post(url_LeTiao,data=data_LeTiao)


# #获取想应状态码
# print(res.status_code)
#
#
# #获取响应信息
# print(res.content)
#
#
# #获取响应体
# print(res.text)
#
#获取json()
print("登录接口:"+str(res.json()))

token_Fetch = res.json()['data']
token =token_Fetch['token']

print("token:"+str(token))


#____________________________________________________________________

# print(type(data_LeTiao))
#
#
# json_LeTiao = json.dumps(data_LeTiao)
#
# print(type(json_LeTiao))



#____________________________________________________________________

#携带token--即关联操作
url_ChangePWD = "http://www.joysurvey.com:8089/survey/man/user/resetPassword"
data_ChangePWD = {'id':'15','password1':'123456789A!','password2':'123456789A!'}
# token = "Bearer" + " " + token

headers={
    "authorization": token
}


res = requests.post(url_ChangePWD,headers=headers)


print(res.json())