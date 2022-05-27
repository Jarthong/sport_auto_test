#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Match_Controller.data_fixture import Match_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_MatchinfoHead(object):
    """获取赛事详情头部信息"""

    @pytest.fixture()
    def public(self,login_train):
        self.base_url = login_train[0] + "/v1/user/_guest/matchInfoHead"
        self.headers = login_train[-1]

    @pytest.mark.parametrize('matchId',[Match_Controller().Match(0)[0],Match_Controller().Match(4)[0],Match_Controller().Match(6)[0],Match_Controller().Match(7)[0]])
    def test_MatchinfoHead(self,public,matchId):
        """
        获取赛事详情头部信息
        :param public:
        :return:
        """
        self.params = {
            "matchId":matchId,
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['matchId'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'




if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))








