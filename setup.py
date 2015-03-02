from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="octopussh",
    version="0.1.0",
    description="SSH Launcher from .sh Bash Scripts",
    license="MIT",
    author="juancarlospaco",
    author_email="JuanCarlosPaco@gmail.com",
    packages=find_packages(),
    install_requires=[],
    scripts=['octopussh'],
    long_description=long_description
)
