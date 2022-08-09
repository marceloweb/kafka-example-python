
import sys

from producer import producer
from consumer import consumer

def main():
  print("Select an option:")
  print("--------------------")
  print("| 1 - Producer     |")
  print("| 2 - Consumer     |")
  print("| 3 - Exit         |")
  print("--------------------")

  print("Input a value: ")
  option = int(input())

  if (option == 3):
     return
  if (option == 1):
     producer()
  if (option == 2):
     consumer()
  return


main()
