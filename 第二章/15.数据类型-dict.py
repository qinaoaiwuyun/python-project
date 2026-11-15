a=[1,2,3,4,5,6,7]
b=["a","b","c","d","e","f","g"]
fler={}
x=0
for i in b:
    fler[i]=a[x]
    x+=1
print(fler)
print(fler["a"])
print(max(fler.values()))


# n=int(input())
# for i in range(n):
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     if sum(a)>sum(b):
#         print(sum(a))
#     elif sum(a)<=sum(b):
#         print(sum(b))

# n=int(input())
# num=[]
# q=[]
# for i in range(n):
#     n,m,k=map(int,input())




