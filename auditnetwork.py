#!/usr/bin/python
'''
1.  the script will verify the SZ for the subnet.
2.  for management and hv it will ensure openstack owns it.
3.  if openstack owns it, it will ensure only that cluster exists and not shared between clusters
4.  if it is hv, it will make sure the network vlan is not used.
'''
def getnet(subn):
    '''
       this would verify the SZ for the subnet.
       this would report who owns it. for management and compute, openstack should own for all new vlans.
    '''
def exclusive_net(subn):
    '''
      this would ensure only that cluster resides on the subnet.
      the network/reserved vlan is not used
    '''
from netaddr import IPNetwork
import argparse
import sys
parser=argparse.ArgumentParser()
#parser.add_argument("-s","--subnet",type=str, required=True)
parser.add_argument("-s","--subnet",type=str)
args=parser.parse_args()
def main():
#    if len(sys.argv) < 2:
#        print 'example usage: python cidrExpand.py cidrRanges.txt >> output.txt'

#    with open(sys.argv[1], 'r') as cidrRanges:
#        for line in cidrRanges:
#            ip = IPNetwork(line)
#            for ip in ip:
#                print ip

#    cidrRanges.close()
#    exit()
    
    a=args.subnet
    print a
if __name__=='__main__':
    main()
