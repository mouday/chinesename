中文取名
========

说明
----

项目包含《百家姓》姓氏504个，常用于名字的汉字2812个
名字汉字中包含大部分《楚辞》、《诗经》词汇

pypi地址： https://pypi.python.org/pypi/chinesename

安装模块
--------

::

    pip install chinesename

代码示例：
----------

.. code:: python

    >>> from chinesename import ChineseName  # 导包

    >>> cn = ChineseName()  # 实例化

    >>> cn.getName()  # 获取一个姓名
    '广袁'

    >>> cn.getNames(10)  # 获取多个姓名
    ['笪递', '慎彭徨', '席具', '锺谦', '任西', '公羊狱', '华桑', '利节', '燕角', '任彪']

    >>> cn.getNameGenerator(10)  # 获取生成器
    <generator object ChineseName.getNameGenerator at 0x1045cfa40>

    >>> cn.getLastName()  # 获取姓氏
    '舒'

    >>> cn.getFirstName()  # 获取名字
    '崔'

    >>> cn.getName(lastname="彭")  # 设置姓氏
    '彭圭'

    >>> cn.getName(char_count=2)  # 设置名字长度
    '倪吏渚'

    >>> cn.getName(sex="boy")  # 设置性别 （boy | girl）
    '骆留'

更新记录
--------

2018年6月20日 修复资源文件导入问题，增加性别参数，区分男孩姓名和女孩姓名
感谢 JoffreyN 提出的建议
`古语云：男楚辞，女诗经。名可以从诗经、楚辞里面取 <https://github.com/mouday/chinesename/issues/2>`__
在原有基础上进行了扩展 遗留问题：取词不准确，需要进一步优化

更新记录
--------

2018年3月19日 修复导入lastnames 和 firstname
文件失败的问题，将两文件内容直接写到chinesename中，并删除两文件

更新记录
--------

2018年1月22日 增加姓名生成器函数，getNameGenerator()
