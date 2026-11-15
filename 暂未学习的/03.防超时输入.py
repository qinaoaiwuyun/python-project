import sys
def solve():
    # 快速读取所有输入
    input_dat=sys.stdin.read().split()
    if not input_dat:# 保护,如果输出为0就停止
        return




    print()
if __name__ == '__main__':# 如果运行这个文件就运行函数
    solve()

# 查分数组
# diff=[0000000000000000000000]
# diff[i]+=2
# diff[q]-=2
# a=0
# ans=[]
# for i in range(n):
#     a+=p[i]
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