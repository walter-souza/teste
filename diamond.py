def draw(n):
  
  for i in reversed(range(0,n)):
    print(" " * i, end="#")
    if (int(2*(n - i) - 1) > 1):
      print(" " * int(2*(n - i) - 3), end="#")
    print()

  for i in range(1,n):
    print(" " * i, end="#")
    if (int(2*(n - i) - 1) > 1):
      print(" " * int(2*(n - i) - 3), end="#")
    print()

  return

n = int(input())

draw(n)    
