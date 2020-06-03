#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


AccessKeyID='LTAI4GBsgbgGLvCpjLbmZNiU'
AccessKeySecret='q42wE5KuTkzcV1oUeS9bSRSR9yDffo'
client = AcsClient(AccessKeyID, AccessKeySecret, 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumbers', "15365385259")
request.add_query_param('SignName', "website")
request.add_query_param('TemplateCode', "SMS_191766627")

response = client.do_action(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))
