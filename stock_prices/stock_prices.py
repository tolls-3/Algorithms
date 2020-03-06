#!/usr/bin/python

import argparse

def find_max_profit(prices):
  curr_min = prices[0]
  curr_max = prices[0]
  profit = 0
  for i in range(0, len(prices)-1):
    diff = prices[i] - curr_min
    if profit == 0 or diff > profit:
      profit = diff
    if prices[i] < curr_min :
      curr_min = prices[i]
    if prices[i] > curr_max:
      curr_max = prices[i]
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))