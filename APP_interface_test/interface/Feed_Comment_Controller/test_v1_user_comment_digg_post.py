from db_fixture.common import GlobalVar
from db_fixture.getdata import GetData

__author__ = 'huxm855'
# -*- coding: utf-8 -*-
import os
import pytest
import requests

condition=""" comment_id not in (select comment_id from feed_comment_digg where USER_ID='{user_id}')""".format(user_id=GlobalVar().GVar_hxm['user_id'])
commentId=[GetData('comment_id','feed_comment',condition).result(), GetData('max(comment_id)','feed_comment',condition).result()+12,None]
seq =range(0,3)
@pytest.mark.parametrize('commentId,seq', list(zip(commentId,seq)))
def test_v1_user_comment_digg(login,commentId,seq):
    ''' 微博评论内容点赞功能接口'''
    base_url =login[0] + "/v1/user/comment/digg"
    params={'commentId':commentId}
    r = requests.post(base_url, headers=login[-1], params=params,verify=False)
    result = r.json()
    print(result)
    if seq == 0:
        assert result['msg']==  '成功'
        assert result['data']== 1
    else :
         assert result['result'] == '4002'


if __name__ == '__main__':
    os.system('pytest -s -v {file}'.format(file=__file__))


