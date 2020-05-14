import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polysdk",
    version="0.0.8",
    author="Fahad Siddiqui",
    author_email="fsid@predictdata.io",
    description="Polymer Python SDK.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polymerhq/polysdk",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests==2.23.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
