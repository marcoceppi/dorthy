from setuptools import setup

install_requires = [
    'tornado',
    'PyYAML'
]

setup(
    name='dorthy',
    version='0.0.1',
    description='A more express.js like framework built on top of Tornado',
    install_requires=install_requires,
    author='Marco Ceppi',
    author_email='marco@ceppi.net',
    url="https://github.com/marcoceppi/dorthy",
    packages=['dorthy']
)
