# 开头:import heapq
# import heapq
# heap=[]
# for num in a:
#     heapq.heappush(heap,num) # 小堆积
#     heapq.heappush(heap,-num) # 用符号模拟大堆积
#
#     cur=-heapq.heappop(heap) # 取出最小值,加-,相当于取出最大值.注意:取出相当于删除,需重新添加
#     heapq.heappush(heap,-new_num) # 重新添加一个数




# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# q=0
# for i in range(n-1):
#     if sum(a[0:i+1])%m==sum(a[i+1:n+1])%m:
#         q+=1
# print(q)
#



n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    b.sort()
    dion={}
    num=0
    s=[]
    p=[]
    for j in b:
        if j in dion:
            dion[j]+=1
        else:
            dion[j]=1
    for k,v in dion.items():
        if v>=2:
            s.append(k)
            for x in range(v-1):
                p.append(k)
            num+=2
        else:
            s.append(k)
            num+=1
    print(num)
    s.sort()
    p.sort()
    p.reverse()
    q=s+p
    print(" ".join(map(str,q)))








