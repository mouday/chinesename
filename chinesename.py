#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import os

class ChineseName(object):
    def __init__(self, firstname_file="firstnames.txt", 
                        lastname_file="lastnames.txt"):
        """初始化
        Args:
            firstname_file: 文件路径 - String
            lastname_file：文件路径 - String
            以上两个路径参数有默认值，也可由用户自定义，文件内容以空格分隔即可
        Returns:
            _firstnames：存储名字，便于多次调用 - List
            _lastnames：存储姓氏，便于多次调用 - List
        """
        self._firstnames=self._getChars(firstname_file)
        self._lastnames=self._getChars(lastname_file)
        
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
  
    def getLastName(self):
        """获取姓氏
        Args:
            None
        Returns:
            String: 姓氏
        """
        lastname = random.choice(self._lastnames)
        return lastname

    def getFirstName(self, char_count=1):
        """获取名字
        Args:
            char_count: 名字长度，默认1 - Integer
        Returns:
            String: 名字
        """
        firstname = []
        for i in range(char_count):
            firstname.append(random.choice(self._firstnames))

        firstname = "".join(firstname)
        return firstname

    def getName(self, char_count=1, lastname=""):
        """获取一个中文名字
        Args:
            char_count: 名字长度，默认1 - Integer
            lastname: 姓氏，默认随机 - String
        Returns:
            String: 名字
        """
        name = []
        if lastname == "":
            name.append(self.getLastName())
        else:
            name.append(lastname)

        name.append(self.getFirstName(char_count))
        name = "".join(name)
        return name

    def getNames(self, count, char_count=1, lastname=""):
        """获取一个中文名字列表
        Args:
            count: 名字数量 - Integer
            char_count: 名字长度，默认1 - Integer
            lastname： 姓氏，默认随机 - String
        Returns:
            List: 名字列表
        """
        names = []
        for i in range(count):
            names.append(self.getName(char_count,lastname))
        return names

def main():
    chinesename = ChineseName()     # 初始化
    name = chinesename.getName(lastname="白")  # 获取一个姓名
    print(name)
    names=chinesename.getNames(100,char_count=2,lastname="彭")   # 获取一个姓名列表
    print(names)


if __name__ == '__main__':
    main()
