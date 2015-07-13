	
def test():
    tenants = {}
    command1 = 'keystone tenant-list'
    for line in os.popen(command1).readlines():
      if not re.search('True',line): continue
      line = line.strip().rstrip('\n')
      flds = re.split('\s+', line,2)
      tenants.setdefault(flds[1], []).append(flds)
    return tenants
def main():
    os.environ['OS_USERNAME']=os.environ['USER']
    os.environ['OS_TENANT_NAME']=sys.argv[1]
    os.environ['OS_AUTH_URL']=sys.argv[2]
    nova = novaclient.v1_1.Client(os.environ['OS_USERNAME'],os.environ['OS_TENANT_NAME'],os.environ['OS_TENANT_NAME'],os.environ['OS_AUTH_URL'])
    print gettenants()
if __name__ == '__main__':
    main()

