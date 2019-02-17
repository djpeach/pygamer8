import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygamer",
    version="0.3.0",
    author="Daniel Peach",
    author_email="dpeachesdev@gmail.com",
    description="An opinionated way to build great games in Pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djpeach/pygamer/releases/tag/0.3.0",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)