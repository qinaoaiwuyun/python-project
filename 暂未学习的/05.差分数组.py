# 查分数组
# diff=[0]*10
# diff[i]+=2
# diff[q]-=2
# a=0
# ans=[]
# for i in range(n):
#     a+=diff[i]
#     ans.append(a)
# 案例
n=5
diff=[0]*n
diff[0]+=2
diff[3]-=2
# diff=[2,0,0,-2.0]
a=0
ans=[]
for i in range(n):
    a+=diff[i]
    ans.append(a)
# diff=[2,2,2,0,0]