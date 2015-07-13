#!/home/y/bin/python2.7
# Script to get list of vm's for a compute node 
from opsDB import opsDB
#import opsDB
import os
import sys
host = sys.argv[1]
in_user = os.environ["USER"]
# USAGE: <script> <user_name>
def usage():
    print "\nUSAGE: SCRIPT <username>\n"
    exit(1)
if len(sys.argv) < 2:
    usage()
else:
#print len(sys.argv)
    my_opsdb = opsDB()
    de_list = my_opsdb.Node.find(parent=sys.argv[1],status="active")

for obj in de_list:
    print obj.name

