# [1,2,3,4]
# output = 1+1+1

def difference(arr):
    ans = 0
    for i in range(1,len(arr)):
        ans += arr[i] - arr[i-1]
    return ans
arr = list(map(int,input("enter number:").strip().split()))
print(difference(arr))