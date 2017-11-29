import chinesename

cnname=chinesename.ChineseName()
name=cnname.getChineseName()
print("name:\n",name)

names=cnname.getChineseNames(100)
print("names:\n",names)