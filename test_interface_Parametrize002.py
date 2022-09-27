import pytest
import requests

# @pytest.mark.parametrize('user,pwd',[['18963988981','123456789A!'],['18988888888','123456789A!']])
# def test_multi_Login(user,pwd):
#
#     url_LeTiao = "http://www.joysurvey.com:8089/survey/man/user/add"
#     data_LeTiao = {'phone':user,'password':pwd}
#
#     #访问登录接口，并获取token。
#
#     res = requests.post(url_LeTiao,data=data_LeTiao)
#
#     print(res.json())
#     # #获取想应状态码
#     print(res.status_code)
#
#
# if __name__ == '__main__':
#     pytest.main()


import pytest
import requests

url_login = 'http://www.joysurvey.com:8089/survey/man/user/add'

@pytest.mark.parametrize('user,phone,pwd1,pwd2,star',[['zhuxu','18963988981','123456789A!','123456789A!','1'],
                         ['zhu','18963988982','123456789!','123456789!','1']])

def test_mu(user,phone,pwd1,pwd2,star):
    data_letiao = {'user':user,'phone':phone,'pwd1':pwd1,'pwd2':pwd2,'star':star}

    res = requests.post(url=url_login,data=data_letiao)
    print(res.json())

    if __name__ == '__main__':
        pytest.main()