#!/usr/bin/python
import socket,sys

# USAGE
def usage():
	print "USAGE: <script> <name>"
	exit(1)

# Invokes all functions
def main(argv=[]):
	argc=len(argv)

	if(argc<2):
		usage()

	name=argv[1]

	if(name==None):
		usage()

	print "==gethostbyname example:=="
	print name + " : " + socket.gethostbyname(name)


	print "==gethostbyname_ex example:=="
	# tuple-1,   tuple-2,          typle-3
	# ("name1", ["name2","name3"], ["ip1", "ip2"])
	(other_name, more_names, ip_list) = socket.gethostbyname_ex(name)
	# process tuple-1
	print "Other name: " + other_name
	# process tuple-2
	for name in more_names:
		print "Name: " + name
	# process tuple-3
	for ipx in ip_list:
		print "Ip: " + ipx



	print "==gethostbyaddr example:=="
	print "Using IP = " + ipx
	#(tuple-1, tuple-2, tuple-3)
	(name, alias_list, addr_list) = socket.gethostbyaddr(ipx)
	# process tuple-1
	print "Name: " + name
	# process tuple-2
	for myalias in alias_list:
		print "Alias: " + myalias
	# process tuple-3
	for addr in addr_list:
		print "Addr: " + addr
	
	

# Execute main now
if __name__ == "__main__":
	main(sys.argv)
