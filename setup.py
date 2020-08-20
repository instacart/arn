# read the contents of your README file
# adapted from https://packaging.python.org/guides/making-a-pypi-friendly-readme/
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
version = (this_directory / "version.txt").read_text().strip()

setup(
    name="arn",
    description="A Python library for parsing AWS ARNs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["dataclasses;python_version<'3.7'"],
    extras_require={
        "dev": [
            "black==19.3b0",
            "flake8==3.7.8",
            "invoke==1.3.0",
            "isort==4.3.21",
            "pytest==5.2.1",
            "pytest-cov==2.8.1",
            "pytest-watch==4.2.0",
            "twine==2.0.0",
            "wheel==0.34.2",
        ]
    },
    version=version,
)
