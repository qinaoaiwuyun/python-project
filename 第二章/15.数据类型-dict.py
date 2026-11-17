# 字典 -- key不能重复(如果重复,后面的值,会覆盖前面的值),key必须得是不可变类型(str,int,float,tuple)
# 定义字典
dict1 ={"王林":670,"李慕婉":608,"徐立国":580,"韩立":688}

print(dict1)
print(type(dict1))

# key必须得是不可变类型(str,int,float,tuple),不能是list,set,dict
dict2 = {0:670,1.5:600,(1,2):500,('A','B'):688}
print(dict2)

# 访问
print(dict1["李慕婉"]) #获取
dict1["李慕婉"] = 688 # 修改
print(dict1)

# --------------------------- 字典 常见操作 ------------------------------------
dict1 ={"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"]=620
print(dict1)

# 查询
print(dict1["涛哥"]) # 根据key获取value
print(dict1.get("涛哥")) # 根据key获取value

print(dict1.keys()) # 获取所有的key
print(dict1.values()) #  获取所有的value
print(dict1.items()) # 获取所有的键值对 key:value

# 删除
score = dict1.pop("许立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)

# 遍历
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]}: {item[1]}")

for k,v in dict1.items():
    print(f"{k}: {v}")









"""
    案例：
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
        1，添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4.查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：XXX，商品价格：XXx，商品数量：xxx"。
        5，退出购物车
        
    结构: shopping_cart = {"Meta80":{"price":6999,"num":2},"鼠标":{...}}
"""
shopping_cart = {}

menu = """
############# 购物车管理系统 ##########
#             1.添加购物车           #
#             2.修改购物车           #
#             3.删除购物车           #
#             4.查询购物车           #
#             5.退出购物车           #
####################################
"""
while True:
    # 1.制作菜单
    print("欢迎使用购物车管理系统~")


    # 2.执行的具体操作
    choice = input("请输入要执行的操作(1-5)")

    match choice:
        case "1": # 添加购物车
            good_name=input("请输入商品名称: ")
            good_price=float(input("请输入商品名称: "))
            good_num=int(input("请输入商品名称: "))

            # 如果商品存在,则不执行添加,提示信息
            if good_name in shopping_cart:
                print("该商品已存在,请重新选择~")
            else:
                shopping_cart[good_name]={"price":good_price,"num":good_num}
                print("商品添加成功~")
        case "2": # 修改购物车
            good_name = input("请输入商品名称: ")

            # 如果商品不存在,则提示错误信息,重新选择
            if good_name not in shopping_cart:
                print("该商品不存在,请重新选择~")
            else:
                good_price = float(input("请输入商品名称: "))
                good_num = int(input("请输入商品名称: "))
                shopping_cart[good_name] = {"price": good_price, "num": good_num}
                print("商品修改成功~")
        case "3": # 删除购物车
            good_name = input("请输入要删除的商品名称: ")

            # 如果商品不存在,则提示错误信息,重新选择
            if good_name not in shopping_cart:
                print("该商品不存在,请重新选择~")
            else:
                del shopping_cart[good_name]
                print("商品删除成功~")
        case "4": # 查询购物车
            for good_name in shopping_cart.keys():
                good_info = shopping_cart[good_name]
                print(f"商品名称: {good_name},商品价格: {good_info['price']},商品数量: {good_info['num']}")
        case "5": # 退出购物车
            print("Bye~")
            break
        case _: #匹配其他情况
            print("非法操作,不支持")