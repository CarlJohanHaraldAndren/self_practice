def combinations(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return combinations(n - 1, k - 1) + combinations(n - 1, k)




def comb2(n,k):
    if k==1:
        return n
    elif n<k:
        return 0
    else:
        return comb2(n - 1, k - 1) + comb2(n - 1, k)

print(comb2(3,2)) #→ 3
print(comb2(10,5)) #→ 252
print(comb2(5,5)) #→ 1