import pytest
import requests
import json


# @pytest.mark.parametrize('user,pwd',[['18963988981','123456789A!'],['18988888888','123456789A!']])
# def multi_Login(user,pwd):
#
#     url_LeTiao = "http://www.joysurvey.com:8089/survey/man/user/login"
#     data_LeTiao = {'phone':user,'password':pwd}
#
#     #访问登录接口，并获取token。
#
#     res = requests.post(url_LeTiao,data=data_LeTiao)
#
#
#     # #获取想应状态码
#     print(res.status_code)
#
#
# #获取响应信息
# print(res.content)
#
#
# #获取响应体
# print(res.text)



#----------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize('user,pwd',[['18963988981','123456789A!'],['18988888888','123456789A!']])
def test_multi_Login(user,pwd):

    url_LeTiao = "http://www.joysurvey.com:8089/survey/man/user/login"
    data_LeTiao = {'phone':user,'password':pwd}

    #访问登录接口，并获取token。

    res = requests.post(url_LeTiao,data=data_LeTiao)

    print(res.json())
    # #获取想应状态码
    print(res.status_code)


if __name__ == '__main__':
    pytest.main()