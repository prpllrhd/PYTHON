from fabric.api import *
import subprocess

import sys
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("cluster")
#parser.add_argument("dir")
#parser.add_argument("role")
#args = parser.parse_args()
#if args.role:
#  env.hosts = subprocess.Popen(["rocl -m -r"+args.role])
#env.hosts=["test01.flurry.gq1.yahoo.com","test02.flurry.gq1.yahoo.com","test03.flurry.gq1.yahoo.com","test04.flurry.gq1.yahoo.com","test05.flurry.gq1.yahoo.com","test06.flurry.gq1.yahoo.com"]


def gethosts(role,help="this is when you specify a role name"):
  thisrole = subprocess.Popen(["rocl -m -r"+role],shell=True,stdout=subprocess.PIPE)
  for i in thisrole.stdout.readlines():
    env.hosts.append(i)
#env.hosts = ['perf-gw.blue.ygrid.yahoo.com','vizorium-gw.blue.ygrid.yahoo.com']
def gethostname():
  run('hostname')
def getspace():
 #  with settings(user="hdfs"):
#  with hide('output','running','warnings'),settings(user="hdfs"):
  with hide('running','warnings'):
    a = run('kinit samy@Y.CORP.YAHOO.COM')
    run("hdfs dfs -df -h")
def getstate():
   a = sudo('kinit hdfs@YGRID.YAHOO.COM -kt /homes/hdfs/hdfs.prod.headless.keytab')
   sudo("hdfs dfsadmin -safemode get")
   sudo("haadmin -getServiceState ha1",user="hdfs")
def gethostsstate(host):
   a = sudo('kinit hdfs@YGRID.YAHOO.COM -kt /homes/hdfs/hdfs.prod.headless.keytab')
   sudo("hdfs dfsadmin -report -live | grep "+host+"| grep Hostname|awk '{print $2}'")
def installsimon():
  try:
    sudo("sudo yum install -y http://cfg.ygrid.yahoo.com:4080/yum/ygrid-el6/daemontools-0.76-8.el6.x86_64.rpm")
  except:
    pass
    run("yinst i simon -br test")
    run("yinst restart simon")
def copysimon():
  sudo("cp /home/samy/simonweb.properties /home/y/conf/simon/simonweb.properties")
  run("yinst start simon")

#def getquota():
#   a = sudo('kinit hdfs@YGRID.YAHOO.COM -kt /homes/hdfs/hdfs.prod.headless.keytab')
#   sudo("hdfs dfs -count -q" + args.dir +  "| awk '{print $8 \" Quota is \" $3/1024/1024/1024/1024 \"Gb and Real size is \" $7/1024/1024/1024/1024*3 \"Gb\"}'")
   
def setupgw():
   sudo("yum -y install ygrid-setup")
   sudo("/usr/local/libexec/setup-gateway")
   sudo("/sbin/service nfs restart")
   sudo("/usr/bin/killall automount")
   sudo("/usr/local/libexec/enable-autofs")
   sudo("/etc/init.d/rpcbind start")
   sudo("/etc/init.d/nfs restart")
   sudo("/usr/local/libexec/enable-autofs")
   sudo("/sbin/chkconfig rpcbind on")
   sudo("/sbin/chkconfig nfs on")
