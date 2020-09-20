import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newline",
    version="0.0.1",
    author="Ayush Sharma",
    author_email="ayushsharma14@gmail.com",
    description="A small package to make it easy to store data in CSV format using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ayush-sharma-py/NewLine.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)