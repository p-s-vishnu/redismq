from setuptools import setup, find_packages

setup(
    name="RedisMQ",
    version="0.1",
    packages=find_packages(exclude=['README.md']),
    install_requires=[
        "redis",
    ],
)
