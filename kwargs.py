#!/usr/bin/python
def test_args(one,*multiple):
  print "Normal: ", one
  for arg in multiple:
    print "*Multiple: ", multiple
def main():
  test_args('sameer','aai','rakhee','yuvaraaj')
if (__name__ == "__main__"):
  main()
