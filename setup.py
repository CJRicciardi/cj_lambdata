# setup.py
'''
lambdata - a collection of data science helper functions
'''

from setuptools import setup, find_packages

REQUIRED = [
    "numpy",
    "pandas",
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
setup(
    name="CJRicciardi-DS-tools",
    version="0.1",
    author="CJ Ricciardi",
    author_email="ricciardistg@gmail.com",
    description="a few convenient data science functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/CJRicciardi/cj_lambdata",
    packages=find_packages(), # ["df_utils"]
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=['Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ]
    )