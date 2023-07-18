from sortedcontainers import SortedList as sl
def countSmaller(nums):
    sortedList,result = sl(list()) ,list()
    for i in range (len(nums)-1,-1,-1):
        n=nums[i]
        index = sortedList.bisect_left(n)
        result.append(index)
        sortedList.add(n)
    return result[::-1]

lis=list(map(int,input().split()))
print(countSmaller(lis))
