def mul(arr):
    n=len(arr)
    result=[]
    for i in range(n):
        for j in range(i+1,n):
            multi=arr[i]*arr[j]
            result.append(multi)

    return result
print(mul([2,3,4]))
# print(sum_absolute_diff_bruteforce([1, 2, 3]))