from setuptools import setup, find_packages

setup(
    name="test_python_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas>=1.1.0",
        "numpy==1.21.0"
    ],
)
