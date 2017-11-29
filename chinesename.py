import random

class ChineseName():

    def __init__(self):
        pass

    # 获取中文字符列表
    # parameters:
    #   filename - 文件路径:string (空格分隔)
    # return:
    #   list - 字符列表
    def getChineseCharacters(self, filename):
        with open(filename, "r") as f:
            ChineseCharacters = f.read().split(" ")
            return ChineseCharacters

    # 获取姓氏
    def getLastName(self):
        lastnames = self.getChineseCharacters("百家姓全文.txt")
        lastname = random.choice(lastnames)
        return lastname

    # 获取名字
    def getFirstName(self, char_count=1):
        firstnames = self.getChineseCharacters("姓名中常用的2897个汉字.txt")
        firstname = []
        for i in range(char_count):
            firstname.append(random.choice(firstnames))

        firstname = "".join(firstname)
        # print(firstname)
        return firstname

    # 获取一个中文名字
    def getChineseName(self, char_count=1, lastname=""):
        ChineseName = []
        if lastname == "":
            ChineseName.append(self.getLastName())
        else:
            ChineseName.append(lastname)

        ChineseName.append(self.getFirstName(char_count))
        ChineseName = "".join(ChineseName)
        return ChineseName

    # 获取一个中文名字列表
    def getChineseNames(self, count, char_count=1, lastname=""):
        ChineseNames = []
        for i in range(count):
            ChineseNames.append(self.getChineseName(char_count,lastname))
        return ChineseNames


def main():
    chinesename = ChineseName()
    name = chinesename.getChineseName(lastname="白")
    print(name)
    names=chinesename.getChineseNames(100)
    print(names)


if __name__ == '__main__':
    main()
