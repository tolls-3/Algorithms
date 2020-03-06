#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0:
    return 1

  total_way = 0

  if n >= 3:
    total_way = total_way + eating_cookies(n - 3)

  if n >= 2:
    total_way = total_way + eating_cookies(n - 2)
  
  if n >= 1:
    total_way = total_way + eating_cookies(n - 1)

  return total_way

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')