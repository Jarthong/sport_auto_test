#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Test_listBusType(object):
    """获取业务类型列表"""

    @pytest.fixture()
    def public(self,login_2):
        self.base_url = login_2[0] + "/v1/serviceCard/listBusType"
        self.headers = login_2[-1]


    def test_listbustype(self,public):
        """
        获取业务类型列表
        :param public:
        :return:
        """
        self.params = {}
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))
















