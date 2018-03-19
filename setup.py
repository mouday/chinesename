
from setuptools import setup, find_packages  
  
setup(  
    name = 'chinesename',  
    version = '0.0.5',
    # keywords = ('chinesename',),  
    description = 'get a chinesename by random',  
    license = 'MIT License',  
    install_requires = [],  
    packages = ['chinesename'],  # 要打包的项目文件夹
    include_package_data=True,   # 自动打包文件夹内所有数据
    author = 'pengshiyu',  
    author_email = 'pengshiyuyx@gmail.com',
    url = 'https://github.com/mouday/chinesename',
    # packages = find_packages(include=("*"),),  
)  
