# -*- coding: utf-8 -*-

# @File    : jieba_split.py
# @Date    : 2018-06-20
# @Author  : Peng Shiyu

# 拆分楚辞和诗经的句子为单个字或词组

import json
import jieba


def read_json(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())


def save_json(filename, lst):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(lst, ensure_ascii=False, indent="\t"))


def jieba_cut(text):
    lst = jieba.lcut(text, cut_all=True)

    # 需要剔除的词
    del_lst = [
        "\u3000",
        "\n",
        "，",
        "。",
        "？",
        "；",
        "?",
        "<",
        "死",
        "",
    ]

    # 去重，去标点符号
    s = set(lst)
    for x in del_lst:
        try:
            s.remove(x)
        except KeyError:
            continue

    # 词组长度进行分组
    dct = {
        "1": [],
        "2": [],
        "0": []
    }
    lst = list(s)
    for x in lst:
        if len(x)==1:
            dct["1"].append(x)
        elif len(x) == 2:
            dct["2"].append(x)
        else:
            dct["0"].append(x)

    return dct


if __name__ == '__main__':
    articles = read_json("gushiwen.json")

    # 楚辞
    dct_chuci = articles.get("楚辞")

    text = "".join([x.get("body") for x in dct_chuci])

    lst = jieba_cut(text)

    save_json("boy.json",lst)

    # 诗经
    dct_shijing = articles.get("诗经")

    text = "".join([x.get("body") for x in dct_shijing])

    lst = jieba_cut(text)

    save_json("girl.json", lst)
