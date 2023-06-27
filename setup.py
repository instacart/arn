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
    url="https://github.com/instacart/arn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    project_urls={
        "Documentation": "https://arn.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/instacart/arn",
    },
    license="BSD 3-Clause Clear License",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["dataclasses;python_version<'3.7'"],
    extras_require={
        "dev": [
            "black==23.3.0",
            "flake8==3.7.8",
            "invoke==1.3.0",
            "isort[pyproject]==4.3.21",
            "pytest==5.2.1",
            "pytest-cov==2.8.1",
            "pytest-watch==4.2.0",
            "twine==2.0.0",
            "wheel==0.34.2",
        ]
    },
    version=version,
)
