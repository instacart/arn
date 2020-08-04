from setuptools import find_packages, setup

setup(
    name="arn",
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
            "Sphinx==3.1.2",
            "twine==2.0.0",
            "wheel==0.34.2",
        ]
    },
    version="0.0.1",
)
