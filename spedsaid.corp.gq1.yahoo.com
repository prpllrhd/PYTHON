#!/usr/bin/env python
import os,argparse
parser=argparse.ArgumentParser()
parser.add_argument('-cl','--cluster',required=True,help="type which cluster, gq1,bf1,ne1. Currently we only have vm's for Grid in gq1")
parser.add_argument('-fn','--function',required=True,help="function of vm's. They could be restapi, gateway for now")
parser.add_argument('-cnt','--count',type=int,default=1,help="count of vm's")
args=parser.parse_args()

login=os.getlogin()
os.environ["OS_USER_NAME"]=login
os.environ["OS_TENANT_NAME"]="grid.us"
os.environ["OS_AUTH_URL"]="http://www.yahoo.com"
print os.getenv("OS_USER_NAME")
print os.getenv("OS_AUTH_URL")

