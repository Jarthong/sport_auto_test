__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from db_fixture.common import GlobalVar, Encrypt


@pytest.mark.parametrize('newPassword', [None, Encrypt().md5Encode(GlobalVar.GVar_hxm['passworld'])])
@pytest.mark.parametrize('oldPassword', [None, Encrypt().md5Encode(GlobalVar.GVar_hxm['passworld'])])
def test_v1_user__password_reset(login, newPassword, oldPassword):
    ''' 修改密码'''
    base_url = login[0] + "/v1/user/_password/reset"
    params = {'account': GlobalVar.GVar_hxm['user_phone'], 'accountType': 3, 'newPassword': newPassword,
              'oldPassword': oldPassword}
    r = requests.post(base_url, headers=login[-1], params=params, verify=False)
    result = r.json()
    print(result)
    if newPassword == None or oldPassword == None:
        assert result['result'] == '4002'
        assert result['msg'] in ('新密码输入不能为空!', '旧密码输入不能为空!')
    else:
        assert result['msg'] == '成功'
        assert result['result'] == '0'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))
