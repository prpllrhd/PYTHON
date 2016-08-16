f = open("file1.txt", 'r') 
x = []; y = []; val = [] 
for line in f: 
    xx, yy, vv = line.split() 
    x.append(float(xx)) 
    y.append(float(yy)) 
    val.append(float(vv)) 
print x

