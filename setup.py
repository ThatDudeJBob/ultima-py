import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uo_sdk-py",
    version="0.0.01",
    author="ThatDudeJBob",
    author_email="thatdudejbob@gmail.com",
    description="uo_sdk-py - UltimaSDK but for Python Scripting use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThatDudeJBob/ultima-py",
    packages=setuptools.find_packages(),
    license="Beerware",
    install_requires=[
        'Pillow',
        'imageio'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
