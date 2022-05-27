#!/user/bin/python
#encoding:utf-8
#__auth__=='__hq__'

import pytest,os
from db_fixture.login_token import *
import  urllib3
from urllib3.exceptions import InsecureRequestWarning

from interface.Search_Controller.data_fixture import Search_Controller

urllib3.disable_warnings(InsecureRequestWarning)


class Test_SearchFeed(object):
    """搜索微博"""

    @pytest.fixture()
    def public(self,login_match):
        self.base_url = login_match[0] + "/v1/search/feed"
        self.headers = login_match[-1]

    keyword = [Search_Controller().feed(),None]
    userId = ['seedp10',None]
    @pytest.mark.parametrize('keyword',keyword)
    @pytest.mark.parametrize('userId',userId)
    def test_searchfeed(self,public,keyword,userId):
        """
        搜索微博
        :param public:
        :return:
        """
        self.params = {
            "keyword":keyword,
            "userId":userId,
            "page":1,
            "rows":15
        }
        r = requests.get(self.base_url,headers = self.headers,verify=False,params=self.params)
        self.result = r.json()
        print(self.result)
        if self.params['keyword'] is not None:
            assert self.result['result'] == '0'
            assert self.result['msg'] == '成功'
        elif self.params['keyword'] is None:
            assert '参数错误' in self.result['msg']


if __name__ == '__main__':
    os.system('pytest -v -s {file}'.format(file=__file__))














