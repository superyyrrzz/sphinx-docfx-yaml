import codecs
from setuptools import setup, find_packages
extra_setup = dict(
install_requires=[
    'PyYAML',
    'wheel==0.24.0',
    'sphinx',
    'unidecode',
],
setup_requires=['pytest-runner'],
tests_require=['pytest', 'mock'],
)

setup(
    name='sphinx-docfx-yaml',
    version='1.1.0',
    author='Eric Holscher',
    author_email='eric@ericholscher.com',
    url='http://github.com/rtfd/sphinx-docfx-yaml',
    description='Sphinx Python Domain to DocFX YAML Generator',
    package_dir={'': '.'},
    packages=find_packages('.'),
    long_description=codecs.open("README.rst", "r", "utf-8").read(),
    # trying to add files...
    include_package_data=True,
    **extra_setup
)
