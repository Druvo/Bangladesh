from setuptools import setup, find_packages


def get_long_description():
    with open('README.rst', 'rb') as f:
        return f.read().decode('utf-8')


VERSION = '0.0.10'
DESCRIPTION = 'A python package For Bangladesh information (District, Division, Thana, post code and etc)'

setup(
    name="bangladesh",
    version=VERSION,
    author="zhdruvo (Zahid Hasan)",
    author_email="<zhdruvo@gmail.com>",
    description=DESCRIPTION,
    long_description=get_long_description(),
    packages=find_packages(),
    license='MIT License',
    include_package_data=True,
    package_data={'': ['data/*.json']},
    url='https://github.com/Druvo/Bangladesh',
    download_url='https://github.com/Druvo/Bangladesh/releases/',
    project_urls={
        'Documentation': 'https://github.com/Druvo/Bangladesh/blob/main/README.md',
        'Source': 'https://github.com/Druvo/Bangladesh',
        'Tracker': 'https://github.com/Druvo/Bangladesh/issues',
    },
    install_requires=[],
    Platform='python',
    keywords=['bangladesh', 'district', 'division', 'thana', 'upazilas'],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: Developers",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Topic :: Communications',
        'Topic :: Education',
        'Topic :: Sociology :: Genealogy',
        'Topic :: System :: Archiving :: Packaging',
    ]

)
