# s = list(input("Enter the string"))

# for i in range(len(s)):
#     condition = False
#     for j in range(len(s)-1):
#         if (ord(s[j])-ord(s[j+1])) == 1:
#             condition = True
#             s[j],s[j+1]=s[j+1],s[j]
#     if condition==False:
#         break

# print(s)

# lst = [21,4,15,17,11,5,40]
# k=3
# x=20

# lst = [abs(i-20) for i in lst]
# lst.sort()
# print(sum(lst[-3:]))

# def sum_of_k_farthest(arr, k, x):
#     diff_arr = [abs(i - x) for i in arr]
    
#     combined_arr = list(zip(arr, diff_arr))
#     print(combined_arr)
#     combined_arr.sort(key=lambda x: x[1], reverse=True)
#     sum_k_farthest = sum(i[0] for i in combined_arr[:k])
#     return sum_k_farthest

# print(sum_of_k_farthest(lst,k,x))


prices = [6,1,3,2,4,7]

lst = [[0 for i in prices] for j in prices]

for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        lst[j][i] = prices[j]-prices[i]

for i in lst:
    print(i)
amt=0
pos=-1
i=len(prices)-1
while i>=0:
    h=-999
    for j in range(len(prices)-1,0,-1):
        print(i,j)
        if lst[i][j]<h:
            h=lst[i][j]
            pos = j
    i-=(pos+1)
# print(amt)