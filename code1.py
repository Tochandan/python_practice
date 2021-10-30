# your code goes here
# take a input integer which is size of list
#2 take a list as input through itetration
#3 again take a for loop from 0 to n-1
#4take empty lst1 in for loop lst1.append ele=lst[i]*lst[i+1]
#5 and print result=,max(lst1)
n=int(input())
lst=[]

for i in range(n):# O(n)
    lst.append(int(input()))
lst.sort()#nlog(n)
maxprod=lst[-1]*lst[-2]
print(maxprod)

n = int(input())
arr = list(map(int, input().split()))#O(n)
c = 0
temp = 0
start = -1
end = -1
f = 0
if len(arr) ==1:
    f = 1
    print( 1, 1, 1)
    return
for i in range(n-1): #TC=O(n-1)
    if(arr[i]<arr[i+1]):
        if(temp==0):
            start = i+1
            temp+=1
    if(temp>c):
        c = temp
    else:
          end = i+1
print(c+1,start,end)
