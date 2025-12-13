#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from setuptools import setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def read(*paths):
    with io.open(os.path.join(BASE_DIR, *paths), encoding="utf-8") as f:
        return f.read()


def find_version():
    version_file = read("dynamic_preferences", "version.py")
    for line in version_file.splitlines():
        if line.startswith("__version__"):
            return line.split("=")[1].strip().strip('"')
    raise RuntimeError("Unable to find version string.")


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


setup(
    name="django-dynamic-preferences",
    version=find_version(),
    description="Dynamic global and instance settings for your django project",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="Agate Blue",
    author_email="me+github@agate.blue",
    url="https://github.com/agateblue/django-dynamic-preferences",
    packages=["dynamic_preferences"],
    include_package_data=True,
    install_requires=[
        "django>=1.11",
        "six",
        "persisting_theory>=0.2.1",
    ],
    license="BSD",
    zip_safe=False,
    keywords="django-dynamic-preferences",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
)
