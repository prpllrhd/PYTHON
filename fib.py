<<<<<<< HEAD
=======
#!/home/y/bin64/python
>>>>>>> b6c13399c281377103be9ad322e2e5bdd56b1e3e
import argparse
def fib(n):
  a,b=0,1
  for i in range(n):
    a,b=b,a+b
  return a
def Main():
  parser=argparse.ArgumentParser(description="fib series pls")
  parser.add_argument("num",help="The Fibonachi Number" + \
			"you wished to calculate",type=int)
  args=parser.parse_args()
  result=fib(args.num)
  print "The " +str(args.num)+"th fib number is " +str(result)

if __name__ == '__main__':
  Main()
