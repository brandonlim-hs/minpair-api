from io import open
from setuptools import find_packages, setup
import os

with open("README.md") as readme_file:
    long_description = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    install_requires = f.read().splitlines()

setup(
    name="app",
    version="1.0.0",
    author="Brandon Lim",
    author_email="brandonlim.lim@gmail.com",
    description="Minimal pairs API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brandonlim-hs/minpair-api",
    packages=find_packages(),
    license="MIT License",
    install_requires=install_requires
)
