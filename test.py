import chinesename  # 导入包

cnname=chinesename.ChineseName()  # 实例化

name=cnname.getChineseName()  # 获取一个中文名
print("name:\n",name)

names=cnname.getChineseNames(100)  # 获取一个中文名列表
print("names:\n",names)

print(cnname.getChineseCharacters.__doc__)  # 测试__doc__