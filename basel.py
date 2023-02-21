def basel(epsilon):
  sum=0
  i=1
  while abs(1/(i**2)) > epsilon:
    sum+=1/(i**2)
    i+=1
  return sum

print(basel(0.0005))

print(len(dir(str)))