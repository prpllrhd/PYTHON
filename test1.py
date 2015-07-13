#!/home/y/bin/python2.6
import argparse
import subprocess as sub
import os, sys
from netaddr import IPNetwork
parser=argparse.ArgumentParser()
parser.add_argument('-c','--cidr',required=True,help='Enter CIDR, example: 10.211.121.64/27')
args=parser.parse_args()
def get_CIDRinfo(subnet):
        ip = IPNetwork(subnet) 
        for ip in ip:
            print ip
def get_subnet(subnet):
    args = [ '/home/y/bin/get_network', subnet ]
    response = sub.Popen(args, stdout=sub.PIPE)
    s_line = response.stdout.readlines()
    try:
        network_id = s_line[0].split()[1]
        mask = s_line[0].split()[2].strip("/")
        #vlan = s_line[0].split()[2].strip("/").split()[6].strip(":")
        owner = ' '.join(s_line[0].split()[-3:-1])
        cidr =  s_line[0].split()[1]
        netinfo=s_line[0].split()[2]
        bp=netinfo.split(":")[3]
        colo=netinfo.split(":")[0]
        sz=netinfo.split(":")[4]
        vlan=netinfo.split(":")[6]
        if "899" in vlan:
            print "flag VLAN: vlan999 is reserved for netops/secops and should not be used for Openstack"
        if "openstack" not in owner.lower():
            print "flag OWNER: CIDR all going forward CIDS's should be owned by Openstack"
        print "Owner: ",owner,"\n","CIDR: ",cidr,"\n","BackPlane: ",bp,"\n","Colo: ",colo,"\n","SZ: ",sz,"\n","Vlan: ",vlan
    except IndexError:
        network_id = 'none'
        mask = 'none'

    return network_id + "/" + mask
    
#cidrRanges.close()
#exit()
if __name__ == '__main__':
    get_subnet(args.cidr)
    get_CIDRinfo(args.cidr)
