#!/home/y/bin/python2.7
import sys
#from IgorAPI import IgorAPI
#my_igor = IgorAPI(user="samy")
'''
if (len(sys.argv)<1):
   print "Error"
'''
cluster=sys.argv[1]
(clustertype,colotype,colo)=cluster.split(".")
if (('cl' in clustertype) &  ('prod' in colotype)):
   print"OSTK::"+colo.upper()+"::OSTK_VM_"+clustertype.upper()+"_MGMT_"+colotype.upper()
   print"OSTK::"+colo.upper()+"::OSTK_VM_"+clustertype.upper()+"_COMPUTE_"+colotype.upper()
   print"OSTK::"+colo.upper()+"::OSTK_VM_ATS_"+clustertype.upper()+"_"+colotype.upper()
elif (('cl' in clustertype) & ('corp' in colotype)):
   print"OSTK::C"+colo.upper()+"::OSTK_VM_"+clustertype.upper()+"_MGMT"
   print"OSTK::C"+colo.upper()+"::OSTK_VM_"+clustertype.upper()+"_COMPUTE"
   print"OSTK::C"+colo.upper()+"::OSTK_VM_ATS_"+colotype.upper()
elif (('dv1' in clustertype) & ('corp' in colotype)):
   print"OSTK::C"+colo.upper()+"::OSTK_OH_CL1_MGMT"
   print"OSTK::C"+colo.upper()+"::OSTK_OH_CL1_COMPUTE"
   print "OSTK::C"+colo.upper()+"::OSTK_OH_CL1_UI_"+colotype.upper()
   print "OSTK::C"+colo.upper()+"::OSTK_OH_ATS_"+colotype.upper()
elif (('cl' in clustertype) &  ('qa' in colotype)):
   print"OSTK::"+colo.upper()+"::OSTK_VM_"+clustertype.upper()+"_COMPUTE_"+colotype.upper()
   print"OSTK::"+colo.upper()+"::OSTK_VM_"+clustertype.upper()+"_MGMT_"+colotype.upper()
   print"OSTK::"+colo.upper()+"::OSTK_VM_ATS_"+clustertype.upper()+"_"+colotype.upper()
elif ('bm' in clustertype):
   print"OSTK::"+colo.upper()+"::OSTK_BM_CL1_MGMT_"+colotype.upper()
   print"OSTK::"+colo.upper()+"::OSTK_BM_ATS_CL1"+"_"+colotype.upper()
   print"OSTK::"+colo.upper()+"::OSTK_BM_CL1_UI_"+colotype.upper()
