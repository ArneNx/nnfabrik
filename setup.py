#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="nnfabrik",
    version="0.0.1",
    description="A generalized model fitting pipeline",
    author="Sinz Lab",
    author_email="software@sinzlab.net",
    packages=find_packages(exclude=[]),
    install_requires=[
        "requests>=2.25.1",
        "sphinx",
        "pytorch_sphinx_theme",
        "recommonmark",
    ],
)
