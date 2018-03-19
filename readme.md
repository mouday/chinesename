# 中文取名
## 说明
项目包含了常用于名字的2812个汉字，常用的姓氏504个

## 代码示例：

```
>>> from chinesename import chinesename  # 导入包

>>> dir(chinesename.ChineseName)  # 查看函数
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__form
at__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_s
ubclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclas
shook__', '__weakref__', '_getChars', 'getFirstName', 'getLastName', 'getName',
'getNameGenerator', 'getNames']

>>> cn = chinesename.ChineseName()  # 实例化

>>> cn.getName()  # 获取中文名
'祖千'

>>> cn.getName(char_count=2) # 指定名长度
'臧炉梗'

>>> cn.getName(lastname="彭")  # 指定姓氏
'彭沥'

>>> cn.getNames(count=10)  # 获取多个中文名
['叶事', '沙舵', '荆奁', '萧叫', '贾塔', '谷圭', '沙宵', '欧句', '年海', '庞伍']

>>> cn.getNames(count=10, char_count=2) # 指定名长度
['饶奔卷', '平楸徐', '侯够畔', '司马履泽', '经回记', '冉血构', '谷锐拒', 
'易毅慧', '终奏舶', '晏陛企']

>>> cn.getNames(count=10, char_count=2, lastname="彭") # 指定姓氏
['彭盲俭', '彭炜拾', '彭僦听', '彭仍艳', '彭滏椅', '彭耳师', '彭铲近', '彭焦与舞
', '彭暮纺', '彭才缘']

>>> cn.getLastName()  # 获取一个姓氏
'石'

>>> cn.getFirstName(char_count=2)  # 获取一个名字
'旗迟'

>>> g=cn.getNameGenerator(count=3)   # 获取一个生成器

>>> g.__next__()
'夏僦'
>>> g.__next__()
'松高'
>>> g.__next__()
'雷喜'
>>> g.__next__()

# 指定名长度，指定姓氏
>>> g=cn.getNameGenerator(count=3, char_count=2, lastname="彭")
>>> g.__next__()
'彭完炮'
>>> g.__next__()
'彭算薛'
>>> g.__next__()
'彭寄投'


```

## 更新记录
2018年1月22日
    增加姓名生成器函数，getNameGenerator()

## 更新记录
2018年3月19日
    修复导入lastnames 和 firstname 文件失败的问题，将两文件内容直接写到chinesename中，并删除两文件


