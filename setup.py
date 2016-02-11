#!/usr/bin/env python
from inspect import cleandoc
from setuptools import setup


def read(path):
    """
    Read the contents of a file.
    """
    with open(path) as f:
        return f.read()


setup(
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Documentation :: Sphinx"],
    name="fusion-kb",
    version="16.0.0",
    description="Fusion Knowledge Base",
    install_requires=[],
    keywords="documentation",
    license="MIT",
    packages=[],
    url="https://github.com/fusionapp/fusion-kb",
    maintainer="Fusion Dealership Systems (Pty) Ltd",
    long_description=read('README.rst'),
    test_suite="txspinneret",
    extras_require={
        "doc": ["Sphinx>=1.3.5",
                "sphinx-rtd-theme>=0.1.9"]})
