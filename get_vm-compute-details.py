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
    
# Main starts here
if len(sys.argv) < 2:
    usage()
else:
    my_opsdb = opsDB()
    hosttype = my_opsdb.Node.find(name = host,status="active")
    de_list = my_opsdb.Node.find(parent = host,status="active")
    
    for ii in hosttype:
        if ii.type == 'vm':
            #print dir(i)
            print "This is a VM"
            print "Hosted on compute node:",ii.parent_name
        elif ii.type == 'host' and ii.property  == 'vm-ops.US':
            print "This is a compute node and following vm's reside on it"
            for obj in de_list:
                 print obj.name
        else:
            print ii.name,"This host does not belong to Openstack. Please check your entry again"     

# End
