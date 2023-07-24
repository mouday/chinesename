import chinesename  # 导入包


def test_chinesename():
    cnname = chinesename.ChineseName()  # 实例化

    assert isinstance(cnname, chinesename.ChineseName)
    name = cnname.getName()  # 获取一个中文名
    print("name:\n", name)

    names = cnname.getNames(100)  # 获取一个中文名列表
    print("names:\n", names)

    print(cnname.getNames.__doc__)  # 测试__doc__

    print(len(cnname._firstnames))
    print(len(cnname._lastnames))

    print(help(chinesename.ChineseName))


def test_getName():
    cn = chinesename.ChineseName()  # 初始化，可以指定姓氏文件
    name = cn.getName(lastname="白", sex="boy")  # 获取一个姓名
    print(name)
    names = cn.getNames(100, char_count=2, lastname="彭")  # 获取一个姓名列表
    print(names)

    # 获取一个姓名生成器
    name_generator = cn.getNameGenerator(10)
    print(name_generator)
