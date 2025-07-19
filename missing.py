def missing(lst):
    sum1=sum(lst)
    num=len(lst)+1
    sum2=num*(num+1)//2
    return sum2-sum1

print(missing([1,2,4,5]))
