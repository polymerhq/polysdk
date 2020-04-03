import setuptools

setuptools.setup(
    name="polysdk",
    version="0.0.1",
    author="Fahad Siddiqui",
    author_email="fsid@predictdata.io",
    description="Polymer Python SDK.",
    long_description_content_type="text/markdown",
    url="https://github.com/polymerhq/polysdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
