from pathlib import Path
from setuptools import setup, find_packages

reqs = Path("requirements.txt").read_text().strip().splitlines()

with open("README.md", "r", encoding="utf-8") as readme:
    readme_contents = readme.read()


setup(
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="A CLI for pyTwistyScrambler, to generate random states for Rubik's cubes/twisty puzzles.",
    install_requires=reqs,
    license="MIT",
    long_description=readme_contents,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="cube puzzle scramble rubiks",
    name="cube scramble cli",
    packages=find_packages(include=["cube_scramble_cli"]),
    entry_points={
        "console_scripts": ["cube-scramble-cli = cube_scramble_cli.__main__:main"]
    },
    url="https://github.com/seanbreckenridge/cube-scramble-cli",
    version="0.4.7",
    zip_safe=False,
)
