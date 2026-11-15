# 元组基本操作 - tupie -----> 元素可以重复,有序,不可修改
# 定义
t1=(80,95,78,50,76,80,85,20)

print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[0:5:1])

# count() 统计元素的个数
print(t1.count(80))

# index() 获取元素的索引(的一个元素的位置)
print(t1.index(80))

# 注意点: 如果定义单元素的元组,单个元素子后需要加上逗号,比如(100,)
t2=()
print(t2)
print(type(t2))

t3=(100)
print(t3)
print(type(t3))


# ----------------元组 tuple 组包和解包----------------------
# 组包操作
t1=(5,7,9,10,2,23,12)
t2=5,7,9,10,2,23,12

print(t1)
print(t2)

# 解包操作
# 基础解包(变量数量与容器的元素个数一致)
a,b,c,d,e,f,g=t1
print(a,b,c,d,e,f,g)

# * 扩展解包 (* 搜集剩余的所有元素,封装列表list中)
first,second,*other,last=t1
print(first,second)
print(other)
print(last)

*other,list2,list1=t1
print(other)
print(list2)
print(list1)

#交换
a,b = b,a






"""
    1.计算每个学生的总分.各科平均分,然后一并输出出来.
    2.统计各科成绩的最低分.最高分.平均分,并输出.
    3.查找成绩优秀(平均分大于90)的学生,并输出.
"""
students=()
