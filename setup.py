from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.8'
DESCRIPTION = 'A python package For Bangladesh information (District, Division, Thana, post code and etc)'
LONG_DESCRIPTION = ''

setup(
    name="bangladesh",
    version=VERSION,
    author="zhdruvo (Zahid Hasan)",
    author_email="<zhdruvo@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    license='MIT License',
    include_package_data=True,
    package_data={'': ['data/*.json']},
    url='https://github.com/Druvo',
    install_requires=[],
    Platform='python',
    keywords=['Bangladesh', 'District', 'Division', 'Thana', 'upazilas'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]
)
