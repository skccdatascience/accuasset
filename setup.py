import setuptools
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install
import warnings

try:
    from accuasset import __prop__
    prop = __prop__.__dict__
except ImportError:
    prop = dict()
    exec(open("accuasset/__prop__.py").read(), prop)

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="accuasset",
    version=prop['__version__'],
    author="hyeonsangjeon",
    author_email="wingnut0310@gmail.com",
    description=prop['__desc__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=prop['__url__'],
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ],
    #package_data = {'' : ['color_maps/*.csv', 'font/*.ttf']},
    package_data = {'' : ['accuasset/domain/eda/*.ttf']},

    #Specify the custom install class
)
