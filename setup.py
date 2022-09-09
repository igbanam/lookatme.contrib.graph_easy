"""
Setup for lookatme.contrib.graph-easy
"""


from setuptools import setup, find_namespace_packages
import os


setup(
    name="lookatme.contrib.graph-easy",
    version="1.0.0",
    description="Introduce ASCII graphs with the Dot notation",
    author="Igbanam",
    author_email="xigbanam@gmail.com",
    python_requires=">=3.5",
    packages=find_namespace_packages(include=["lookatme.*"]),
)
