import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="customLogger",
    version="0.0.1",
    author="Shahram Khalid",
    author_email="shahramkhalid01@gmail.com",
    description="Package to return custom logger objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["customLogger"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
