def binarySearch(values,i,j,key):
    if i > j:
        return None
    k = (i + j) // 2
    if values[k] > key:
        return binarySearch(values, i, k - 1, key)
    elif values[k] < key:
        return binarySearch(values, k + 1, j, key)
    else:
        return k



print(binarySearch([1, 5, 7, 8],0,3,5)) # → 1
print(binarySearch([1, 5, 7, 8],0,3,10)) # → None
print(binarySearch([1, 5, 7, 8],0,3,0)) # → None
print(binarySearch([1, 5, 7, 8],2,3,5)) # → None
print(binarySearch(['a', 'b', 'c'],0,2,'b')) # → 1