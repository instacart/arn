# Contributing to `arn`

## Reporting issues

To report an issue, use the [Issues tab](https://github.com/instacart/arn/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) to search for an existing issue that matches what you are experiencing. If you can't find one, open a new issue, providing as much detail as you can.

## Making a contribution

### Development
To work on `arn`, first fork this repository, then clone it locally:
```bash
git@github.com:<username>/arn.git
```
where `<username>` is your GitHub username.

### Dependencies
`arn` requires [pyenv](https://github.com/pyenv/pyenv) to be installed, to enforce that all developers use the same version of Python.

Once pyenv is available, install PyPI dependencies by running
```bash
source script/bootstrap
```
This command will ensure that the correct version of Python is installed, create a virtualenv if necessary, source it, and install all dependencies and development dependencies in it. The script is idempotent, so it's safe to always source it when opening a new terminal 

### Concepts
The main source code of the library is in `src/arn`, generally with one Python file per AWS service (IAM, S3, etc). 

To create a new type of ARN, simply subclass the existing `Arn` class and define the pattern that represents that ARN using a regex with named capturing groups:
```python
from arn import Arn

class MyResourceArn(Arn):
    REST_PATTERN = r"myresource/(?P<foo>.*)"
```

When a user parses an ARN string with this class, the resulting `MyResourceArn` instance will have a `foo` property with the value that was captured by the regex:
```python
arn = MyResourceArn("arn:aws:myservice:us-east-1:123456789012:myresource/bar")
assert arn.foo == "bar"
```

### Conventions
We use tools to enforce code quality in this repo. We use [black](https://black.readthedocs.io/en/stable/) to maintain a unified code style, [isort](https://timothycrosley.github.io/isort/) to enforce a unified import order, and [flake8](https://flake8.pycqa.org/en/latest/) to catch lint errors.

All these tools are invoked using [invoke](http://www.pyinvoke.org/), which is a Make-style task runner. The following lint-related tasks are available:
```bash
$ inv -l
  black          Format your code base using black.
  black-check    Check if your code base is formatted with black.
  flake8-check   Lint your code using flake8.
  format         Format your code with black and isort.
  isort          Sort your imports.
  isort-check    Check if your imports have been sorted properly.
  lint           Lint your code with flake8 and check the formatting with black and isort.
```

### Tests
We use [pytest](https://docs.pytest.org/en/latest/) to run tests, and all classes in `arn` should have some. To run them, simply run
```bash
pytest
```

When addig a new ARN class, please also add tests to cover the new behaviour.
