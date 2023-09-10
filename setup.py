import setuptools

setuptools.setup(
    name="retropy",
    version="0.1.0",
    url="https://github.com/jowo8jowo/retropy.git",
    author="Jowo",
    author_email="jowo8jowo@gmail.com",
    description="Downloads, parses Retrosheet data from Retrosheet.org",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
)
