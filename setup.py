# -*- encoding: utf-8 -*-

import setuptools
import os
import io

# 将markdown格式转换为rst格式
# def md_to_rst(from_file, to_file):
#     r = requests.post(url='http://c.docverter.com/convert',
#                       data={'to':'rst','from':'markdown'},
#                       files={'input_files[]':open(from_file,'rb')})
#     if r.ok:
#         with open(to_file, "wb") as f:
#             f.write(r.content)

# if os.path.exists( "README.md"):
#     md_to_rst("README.md", "README.rst")

# long_description = 'Add a fallback short description here'
# if os.path.exists('README.rst'):
#     long_description = io.open('README.rst', encoding="utf-8").read()

with io.open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="chinesename",
    version="0.1.1",
    author="Peng Shiyu",
    author_email="pengshiyuyx@gmail.com",
    description="get a chinesename by random",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/mouday/chinesename",
    packages=setuptools.find_packages(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        # 'Programming Language :: Python :: 3.13',
        # 'Programming Language :: Python :: 3.14',
        # 'Programming Language :: Python :: 3.15',
        # 'Programming Language :: Python :: 999.99',
    ),
    zip_safe=True,
    include_package_data=True,
    install_requires=[],  # 常用
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        'chinesename': ['source/*.txt', "source/*.json"],
    },
)
