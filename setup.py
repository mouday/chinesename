import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chinesename",
    version="0.0.7",
    author="Peng Shiyu",
    author_email="pengshiyuyx@gmail.com",
    description="get a chinesename by random",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mouday/chinesename",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    package_data = {
            # If any package contains *.txt or *.rst files, include them:
            '': ['source/*.txt', "source/*.json"],
    }
)
