import setuptools
from distutils.util import convert_path

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="BioPro",
    version="0.1.7",
    author="Tianqin Li, Zeyuan Zuo, Jui-Chia Chung, Serena Abraham, Snigdha Agarwal",
    author_email="jacklitianqin@gmail.com",
    description="BioPro is a bioinformatics pipeline that predicts the functional targets of RNA-binding protein and the biological processes to which these functional targets contribute. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Crazy-Jack/SuperdopeBioinformatics",
    packages=['Team3'],
    entry_points = {
        'console_scripts':[
            'BioPro = Team3.__main__:main',
            ]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
)
