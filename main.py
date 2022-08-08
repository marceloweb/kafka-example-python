import sys
sys.path.insert(0, './producer')
from main.py import producer


def main():
  print("Select an option:")
  print("--------------------")
  print("| 1 - Producer     |")
  print("| 2 - Consumer     |")
  print("--------------------")

  option = input("Input a value: ")
  print(option)
  return


main()
