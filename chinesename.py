import random

class ChineseName(object):

    def __init__(self):
        pass

    def getChineseCharacters(self, filename):
        """获取中文字符列表
        Args:
            filename: 文件路径 - String (空格分隔文件)
        Returns:
            List: 字符列表
        """
        with open(filename, "r") as f:
            ChineseCharacters = f.read().split(" ")
            return ChineseCharacters
  
    def getLastName(self):
        """获取姓氏
        Args:
            None
        Returns:
            String: 姓氏
        """
        lastnames = self.getChineseCharacters("百家姓全文.txt")
        lastname = random.choice(lastnames)
        return lastname

    def getFirstName(self, char_count=1):
        """获取名字
        Args:
            char_count: 名字长度，默认1 - Integer
        Returns:
            String: 名字
        """
        firstnames = self.getChineseCharacters("姓名中常用的2897个汉字.txt")
        firstname = []
        for i in range(char_count):
            firstname.append(random.choice(firstnames))

        firstname = "".join(firstname)
        return firstname

    def getChineseName(self, char_count=1, lastname=""):
        """获取一个中文名字
        Args:
            char_count: 名字长度，默认1 - Integer
            lastname: 姓氏，默认随机 - String
        Returns:
            String: 名字
        """
        ChineseName = []
        if lastname == "":
            ChineseName.append(self.getLastName())
        else:
            ChineseName.append(lastname)

        ChineseName.append(self.getFirstName(char_count))
        ChineseName = "".join(ChineseName)
        return ChineseName

    def getChineseNames(self, count, char_count=1, lastname=""):
        """获取一个中文名字列表
        Args:
            count: 名字数量 - Integer
            char_count: 名字长度，默认1 - Integer
            lastname： 姓氏，默认随机 - String
        Returns:
            List: 名字列表
        """
        ChineseNames = []
        for i in range(count):
            ChineseNames.append(self.getChineseName(char_count,lastname))
        return ChineseNames

def main():
    chinesename = ChineseName()
    name = chinesename.getChineseName(lastname="白")
    print(name)
    names=chinesename.getChineseNames(100,char_count=2,lastname="彭")
    print(names)


if __name__ == '__main__':
    main()
