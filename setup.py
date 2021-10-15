from setuptools import setup

setup(
    name="Aeon",
    version="0.0.1",
    author="xeeny",
    author_email="xeeny@wp.pl",
    description="JVM in python",
    license="MIT",
    packages=["aeon"],
    entry_points={
        'console_scripts': ['aeon=aeon.aeon:main']
    },
)
