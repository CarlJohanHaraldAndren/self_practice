def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(gcd(84, 60)) #12
print(gcd(10,5)) #5
print(gcd(12,20)) #4
print(gcd(99,0))#99
print(gcd(0,99)) #99