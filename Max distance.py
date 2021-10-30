'''
'''
# your code goes here
#Distance(arr[i],arr[j]) = (i x arr[i]-j x arr[j]) - (arr[i]+arr[j])==>(i-1)x(arr[i)-(j+1)x(arr[j])
n=int(input())
arr=[int(x) for x in input().split()]
first=[]
second=[]
for x in range(n):
	first.append((x-1)*arr[x])  #(i-1)x(arr[i)
	second.append((x+1)*arr[x])  #(j+1)x(arr[j])
print(max(first)-min(second))