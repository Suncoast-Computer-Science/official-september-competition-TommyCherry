a = str(input())
b = str(input())
if len(b) < len(a):
  c = b + a
else:
  c = a + b
d = int(input())

if len(c) == d:
  print(c)
else:
  print("False")
