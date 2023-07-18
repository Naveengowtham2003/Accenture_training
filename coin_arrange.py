def coin_arrange(n):

    left,right,result = 1,n,0
    while left<=right:
        mid=(left+right)//2
        coins= (mid/2)*(mid+1)
        if coins>n:
            right = mid-1
        else:
            left  = mid+1
            result = max(mid,result)
    return result

n=int(input())
print(coin_arrange(n))
