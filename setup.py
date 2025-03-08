from setuptools import setup, find_packages

setup(
    name="menupy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # List dependencies here
    author="Venom <3",
    description="A simple Python library to add menus and titles to your level!",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/venom-kitty/menupy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
