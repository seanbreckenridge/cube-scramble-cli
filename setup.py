#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['colorama>=0.4.1', 'prompt_toolkit>=2.0.8', 'pyTwistyScrambler>=1.2']

setup(
    author="Sean Breckenridge",
    author_email='seanbrecke@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A simple CLI for pyTwistyScrambler, to generate random states for twisty puzzles.",
    install_requires=requirements,
    license="MIT",
    long_description="Requires Python 3.6 | 3.7.\n\n" + \
                    "Installation: python3 -m pip install cube-scramble-cli\n\n" + \
                    "Run: $ scramble-cli\n\n" + \
                    "More info here: https://github.com/seanbreckenridge/cube-scramble-cli",
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='cube puzzle scramble',
    name='cube scramble cli',
    packages=find_packages(include=['cube_scramble_cli']),
    scripts=['cube_scramble_cli/scramble-cli'],
    url='https://github.com/seanbreckenridge/cube-scramble-cli',
    version='0.1.0',
    zip_safe=False,
)
