'''
author:lance.lan
date:2023/5/31
project:shopping
'''
from rest_framework.response import Response

from rest_framework.response import Response
class APIResponse(Response):
    def __init__(self, code=100, message='成功', data=None, status=None, headers=None, **kwargs):
        dic = {'code': code, 'message': message}
        if data:
            dic['data'] = data
        dic.update(kwargs)  # 可以灵活的添加，需要返回的键值对
        super().__init__(data=dic, status=status, headers=headers)