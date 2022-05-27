#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
from interface.Match_Controller.data_fixture import *
from interface.Community_Controller.data_fixture import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_listMatchByCondition(object):
    """根据条件查询赛事列表"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/user/listMatchByCondition"
        self.headers = login_train[-1]

    matchStatus = [3,4,5,6]
    matchIpRecomId = [Match_Controller().User_info()]
    @pytest.mark.parametrize('matchStatus',matchStatus)
    @pytest.mark.parametrize('matchIpRecomId',matchIpRecomId)
    def test_listmatchByCondition(self,public,matchStatus,matchIpRecomId):
        """
        根据条件查询赛事列表
        :param public:
        :return:
        """
        self.params = {
            "matchIpRecomId":matchIpRecomId,
            "matchFormat":1,
            "matchStatus":matchStatus,
            # "cityId": 15,
            "page": 1,
            "rows":10
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['matchStatus'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        # elif self.params['matchId'] is None:
        #     assert '不能为null' in self.result['msg']
        #     assert self.result['result'] == '4002'
        # elif self.params['matchId'] == 2275:
        #     assert '该赛事类型暂没有排名' in self.result['msg']
        #     assert self.result['result'] == '9028'



if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))

