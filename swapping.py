tc = int(input())

def swap(string):
      
    # storing the first character
    start = string[0]
      
    # storing the last character
    end = string[-1]
      
    swapped_string = end + string[1:-1] + start
    print(swapped_string)
      
# Driver Code
while tc > 0:
  name = input()
  swap(name)
  tc -= 1
