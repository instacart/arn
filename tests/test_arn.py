import re

import pytest

from arn import Arn, InvalidArnException, InvalidArnRestException

from .conftest import make_arn


def test_parse_arn_basic():
    arn = make_arn("service", "rest")
    result = Arn(arn)
    assert result.partition == "aws"
    assert result.service == "service"
    assert result.region == "us-east-1"
    assert result.account == "123456789"
    assert result.rest == "rest"


@pytest.mark.parametrize("field", ["partition", "service", "region", "account"])
def test_override_field(field):
    arn = make_arn("service", "rest")
    result = Arn(arn, **{field: "override"})
    assert getattr(result, field) == "override"


@pytest.mark.parametrize("arn", ["arn:aws::::"])
def test_parse_arn_invalid(arn):
    with pytest.raises(InvalidArnException):
        Arn(arn)


@pytest.mark.parametrize("arn", ["arn:aws:service:region:account:foo"])
def test_parse_arn_invalid(arn):
    class CustomArn(Arn):
        REST_PATTERN = re.compile(r"notfoo")

    with pytest.raises(InvalidArnRestException):
        CustomArn(arn)
