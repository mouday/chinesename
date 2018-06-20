#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import random
import os

# 限定可见方法
__all__ = ["ChineseName"]

#================
# 资源文件
#================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LASTFILE = os.path.join(BASE_DIR, "source/lastnames.txt")
FIRSTFILE = os.path.join(BASE_DIR, "source/firstnames.txt")

BOYFILE = os.path.join(BASE_DIR, "source/boy.json")
GIRLFILE = os.path.join(BASE_DIR, "source/girl.json")


#===================
# 主体代码
#===================
class ChineseName(object):
    """中文名取名"""
    def __init__(self, firstname_file=FIRSTFILE, lastname_file=LASTFILE):
        """初始化
        Args:
            firstname_file: 名字文件路径 - String
            lastname_file：姓氏文件路径 - String
            以上两个路径参数有默认值，也可由用户自定义，文件内容以空格分隔即可
        """
        # 存储名字，便于多次调用 - List
        self._firstnames = self._getChars(firstname_file)

        # 存储姓氏，便于多次调用 - List
        self._lastnames = self._getChars(lastname_file)

        self._loadFirstName()

    def _getChars(self, filename):
        """获取中文字符列表
        Args:
            filename: 文件路径 - String (空格分隔文件)
        Returns:
            List: 字符列表
        Raise:
            file not find
        """
        if os.path.exists(filename):
            with open(filename, "r") as f:
                chars = f.read().split(" ")
                return chars
        else:
            raise IOError("file not find!")

    def _loadFirstName(self):
        """
        加载男孩女孩名字
        """
        # 加载男孩名字 {dict}
        with open(BOYFILE, "r") as f:
            self._boy_firstnames = json.loads(f.read())

        # 加载女孩名字 {dict}
        with open(GIRLFILE, "r") as f:
            self._girl_firstnames = json.loads(f.read())

    def getLastName(self):
        """获取姓氏
        Args:
            None
        Returns:
            String: 姓氏
        """
        return random.choice(self._lastnames)

    def _getFirstName(self, char_count=1, sex="boy"):
        """
        获取名字
        :param char_count: {int} 名字字数
        :param sex: {str} 性别 (boy | girl)
        :return: {srt} 名字
        """
        firstnames = {
            "boy": self._boy_firstnames,
            "girl": self._girl_firstnames
        }

        try:
            return random.choice(firstnames.get(sex).get(str(char_count)))
        except KeyError:
            raise KeyError("please input char_count between 1-2")

    def getGirlFirstName(self, char_count=1):
        """
        获取一个女孩名字
        :param char_count:  {int} 名字字数
        :return: {str} 名字
        """
        return self._getFirstName(char_count, sex="boy")

    def getBoyFirstName(self, char_count=1):
        """
        获取一个男孩名字
        :param char_count:  {int} 名字字数
        :return: {str} 名字
        """
        return self._getFirstName(char_count, sex="girl")

    def getFirstName(self, char_count=1, sex=None):
        """获取名字
        Args:
            char_count: {int} 名字长度，默认1
            sex: {str} 性别(boy | girl)
        Returns:
            String: 名字
        """
        if sex == "boy":
            firstname = self.getBoyFirstName(char_count)

        elif sex == "girl":
            firstname = self.getGirlFirstName(char_count)

        else:
            firstname = []
            for i in range(char_count):
                firstname.append(random.choice(self._firstnames))

            firstname = "".join(firstname)

        return firstname

    def getName(self, char_count=1, lastname="", sex=None):
        """获取一个中文姓名
        Args:
            char_count: 名字长度，默认1 - Integer
            lastname: 姓氏，默认随机 - String
            sex: {str} 性别(boy | girl)
        Returns:
            String: 姓名
        """
        name = []
        if lastname == "":
            name.append(self.getLastName())
        else:
            name.append(lastname)

        name.append(self.getFirstName(char_count, sex))
        name = "".join(name)
        return name

    def getBoyName(self, char_count=1, lastname=""):
        """
        获取男孩姓名
        :param char_count: {int} 名字长度，默认1
        :param lastname: {str} 姓氏 默认随机
        :return: {str} 姓名
        """
        return self.getName(char_count, lastname, sex="boy")

    def getGirlName(self, char_count=1, lastname=""):
        """
        获取女孩姓名
        :param char_count: {int} 名字长度，默认1
        :param lastname: {str} 姓氏 默认随机
        :return: {str} 姓名
        """
        return self.getName(char_count, lastname, sex="girl")

    def getNames(self, count, char_count=1, lastname="", sex=None):
        """获取一个中文姓名列表
        Args:
            count: 名字数量 - Integer
            char_count: 名字长度，默认1 - Integer
            lastname： 姓氏，默认随机 - String
            sex: {str} 性别(boy | girl)
        Returns:
            List: 姓名列表
        """
        names = []
        for i in range(count):
            names.append(self.getName(char_count, lastname, sex))
        return names

    def getNameGenerator(self, count, char_count=1, lastname="", sex=None):
        """获取一个中文姓名生成器，2018年1月22日
        Args:
            count: 名字数量 - Integer
            char_count: 名字长度，默认1 - Integer
            lastname： 姓氏，默认随机 - String
            sex: {str} 性别(boy | girl)
        Returns:
            Yield：姓名生成器
        """
        for i in range(count):
            yield self.getName(char_count, lastname, sex)
        

def main():
    chinesename = ChineseName()     # 初始化，可以指定姓氏文件
    name = chinesename.getName(lastname="白", sex="boy")  # 获取一个姓名
    print(name)
    names=chinesename.getNames(100,char_count=2,lastname="彭")   # 获取一个姓名列表
    print(names)

    # 获取一个姓名生成器
    name_generator = chinesename.getNameGenerator(10)
    print(name_generator)

if __name__ == '__main__':
    main()
