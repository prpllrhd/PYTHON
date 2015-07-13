#!/bin/env python
import sys
import os
dv1_corp_gq1 = "http://keystoneservice.ostk.dv1.vip.corp.gq1.yahoo.com:5000/v2.0"
dv1_corp_sg3 = "http://keystoneservice.ostk.dv1.vip.corp.sg3.yahoo.com:5000/v2.0"
dv1_corp_ir2 = "http://keystoneservice.ostk.dv1.vip.corp.ir2.yahoo.com:5000/v2.0"
dv1_corp_ne1 = "http://keystoneservice.ostk.dv1.vip.corp.ne1.yahoo.com:5000/v2.0"
cl1_corp_bf1 = "http://keystone-service.openstack.corp.bf1.corp.yahoodns.net:5000/v2.0"
cl1_corp_ne1 = "http://keystone.ostk.cl1.vip.corp.ne1.yahoo.com:5000/v2.0"
cl1_corp_gq1 = "http://keystone-service.openstack.corp.gq1.corp.yahoodns.net:5000/v2.0"
cl1_corp_sg3 = "http://keystone.ostk.cl1.vip.corp.sg3.yahoo.com:5000/v2.0"
cl1_prod_gq1 = "http://keystoneservice.ostk.cl1.prod.vip.gq1.yahoo.com:5000/v2.0"
cl1_prod_bf1 = "http://keystoneservice.ostk.cl1.prod.vip.bf1.yahoo.com:5000/v2.0"
cl3_prod_bf1 = "http://keystoneservice.ostk.cl3.prod.vip.bf1.yahoo.com:5000/v2.0"
cl3_prod_gq1 = "http://keystoneservice.ostk.cl3.prod.vip.gq1.yahoo.com:5000/v2.0"
cl1_qa_bf1 = "http://keystone-service.openstack.bf1.corp.yahoodns.net:5000/v2.0"
cl1_qa_gq1 = "http://keystone-service.openstack.gq1.corp.yahoodns.net:5000/v2.0"
cl1_qa_ne1 = "http://keystoneservice.ostk.cl1.qa.vip.ne1.yahoo.com:5000/v2.0"


username = os.environ["USER"] 
os.environ['OS_TENANT_NAME']='admin'
os.environ['OS_USERNAME']=username
if sys.argv[1] == cl1_prod_gq1:
    os.environ['OS_AUTH_URL'] = cl1_prod_gq1
elif sys.argv[1] == cl1_prod_bf1:
    os.environ['OS_AUTH_URL'] = cl1_prod_bf1
elif sys.argv[1] == cl3_prod_bf1:
    os.environ['OS_AUTH_URL'] = cl3_prod_bf1
elif sys.argv[1] == cl3_prod_gq1:
    os.environ['OS_AUTH_URL'] = cl3_prod_gq1
elif sys.argv[1] == cl1_corp_gq1:
    os.environ['OS_AUTH_URL'] = cl1_corp_gq1
elif sys.argv[1] == cl1_corp_bf1:
    os.environ['OS_AUTH_URL'] = cl1_corp_bf1
elif sys.argv[1] == cl1_corp_ne1:
    os.environ['OS_AUTH_URL'] = cl1_corp_ne1
elif sys.argv[1] == cl1_corp_sg3:
    os.environ['OS_AUTH_URL'] = cl1_corp_sg3
elif sys.argv[1] == cl1_qa_bf1:
    os.environ['OS_AUTH_URL'] = cl1_qa_bf1
elif sys.argv[1] == cl1_qa_gq1:
    os.environ['OS_AUTH_URL'] = cl1_qa_gq1
elif sys.argv[1] == cl1_qa_ne1:
    os.environ['OS_AUTH_URL'] = cl1_qa_ne1
elif sys.argv[1] == dv1_corp_ne1:
    os.environ['OS_AUTH_URL'] = dv1_corp_ne1
elif sys.argv[1] == dv1_corp_gq1:
    os.environ['OS_AUTH_URL'] = dv1_corp_gq1
elif sys.argv[1] == dv1_corp_sg3:
    os.environ['OS_AUTH_URL'] = dv1_corp_sg3
elif sys.argv[1] == dv1_corp_ir2:
    os.environ['OS_AUTH_URL'] = dv1_corp_ir2
abc =os.popen("nova list")
print abc
