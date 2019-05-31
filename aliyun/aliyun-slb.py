#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAIQaG61OfYmuju', 'MHyznySRPs8bwBjaE3qqmv303jYyk3', 'cn-hongkong')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('slb.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('http') # https | http
request.set_version('2014-05-15')
request.set_action_name('ModifyLoadBalancerInternetSpec')

request.add_query_param('RegionId', 'cn-hongkong')
request.add_query_param('LoadBalancerId', 'lb-j6c8l2itj69u3ty6495f8')
request.add_query_param('Bandwidth', '35')
request.add_query_param('InternetChargeType', 'paybybandwidth')
request.add_query_param('AutoPay', 'false')

response = client.do_action(request)
# python2:  print(response) 
print(str(response, encoding = 'utf-8'))
