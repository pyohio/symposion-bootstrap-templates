#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name="symposion-bootstrap-templates",
    author="Christopher Neugebauer",
    author_email="_@chrisjrn.com",
    version="0.0.1-dev11",
    description="Default templates for Symposion",
    url="http://github.com/chrisjrn/symposion-bootstrap-templates/",
    packages=find_packages(),
    include_package_data=True,
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT licence",
    ),
)
