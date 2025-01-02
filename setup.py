import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="readInstruments",
    version="0.1",
    author="John A. Sorensen",
    author_email="john.sorensen@usda.gov",
    description="Read Instrument data from GSWRL Temple, TX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages()
)