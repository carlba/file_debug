import os

from setuptools import setup, find_packages
from distutils.cmd import Command

NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


class BootStrap(Command):

    """setuptools Command"""

    description = "run my command"

    user_options = []

    def initialize_options(self):
        """Abstract method that is required to be overwritten"""

    def finalize_options(self):
        """Abstract method that is required to be overwritten"""

    def run(self):

        print(" => bootstrapping development environment ...")
        self.mkpath("src")
        package_dir = os.path.join("src", NAME)
        self.mkpath(package_dir)
        touch(os.path.join("src", "__init__.py"))
        touch(os.path.join(package_dir, "__init__.py"))
        touch(os.path.join(package_dir, NAME + ".py"))

# Sample install requires list ['Twisted==13.0.0']

setup(name=NAME,
      version='0.0.1',
      packages=find_packages("src"),
      package_dir={'': 'src'},
      include_package_data=True,
      author='Birdstep Technology',
      author_email='support@birdstep.com',
      install_requires=[],
      cmdclass={
          'boot_strap': BootStrap
      })
