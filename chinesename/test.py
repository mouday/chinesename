import chinesename  # 导入包

cnname=chinesename.ChineseName()  # 实例化

name=cnname.getName()  # 获取一个中文名
print("name:\n",name)

names=cnname.getNames(100)  # 获取一个中文名列表
print("names:\n",names)

print(cnname.getNames.__doc__)  # 测试__doc__

print(len(cnname._firstnames))
print(len(cnname._lastnames))