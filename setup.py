from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
      name = 'ras2df',
      version = '0.0.1',
      description = 'Converts raster data into pandas dataframe',
      py_modules = ["ras2df"],
      package_dir = {'':'src'},
      classifiers = [
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.8.8",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          ],
      long_description = long_description,
      long_description_content_type="text/markdown",
      url = "https://github.com/RJLA/ras2df.git",
      author = 'Reginald Argamosa',
      author_email = "<regi.argamosa@gmail.com>",
      install_requires=required,
)