#!/home/y/bin/python2.6
import argparse
#from opsDB import opsDB
import os
import sys
#parser = argparse.ArgumentParser
#parser.add_argument('hosts',nargs='+',type=string)
#args = parser.parse_args()
def main():
  # getHV(sys.argv[1])
    getvms()

def getHV(compute):
    in_user = os.environ["USER"]
    my_opsdb = opsDB()
    de_list = my_opsdb.Node.find(parent=compute,status="active")
    for obj in de_list:
       print obj.name
def getvms():
    nova = novaclient.v1_1.Client(os.environ['OS_USERNAME'], os.environ['OS_PASSWORD'], os.environ['OS_TENANT_NAME'], os.environ['OS_AUTH_URL'])
    for line in os.popen('nova list'):
        print line
    

if __name__ == '__main__':
  main()
