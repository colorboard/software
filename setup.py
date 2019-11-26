from setuptools import setup, find_packages
from colorware import __version__

setup(
    name='colorware',
    version=__version__,
    author='Robotesla',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'flask', 'flask_restful'
    ]
)
