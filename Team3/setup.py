import setuptools
from distutils.util import convert_path

with open("README.md", "r") as fh:
    long_description = fh.read()


main_ns = {}
ver_path = convert_path('version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name="BioPro",
    version=main_ns['__version__'],
    author="",
    author_email="",
    description=" python package ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Crazy-Jack/SuperdopeBioinformatics",
    packages=['Team3'],
    entry_points = {
        'console_scripts':[
            #'circDraw = circDraw.__main__:main',
            'Team3 = Team3.__main__:main',
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
