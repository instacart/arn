import re

import pytest

from arn import (
    Arn,
    ConflictingFieldNamesException,
    InvalidArnException,
    InvalidArnRestException,
)

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


def test_str():
    arn = make_arn("service", "rest")
    result = Arn(arn)
    assert str(result) == arn


def test_str_with_overridden_field():
    arn = make_arn("service", "rest")
    result = Arn(arn, partition="foo")
    assert str(result) == "arn:foo:service:us-east-1:123456789:rest"


@pytest.mark.parametrize("arn", ["arn:aws::::"])
def test_parse_arn_invalid(arn):
    with pytest.raises(InvalidArnException, match="arn:aws:::: is not a valid ARN"):
        Arn(arn)


@pytest.mark.parametrize("arn", ["arn:aws:service:region:account:foo"])
def test_parse_arn_invalid_rest(arn):
    class CustomArn(Arn):
        REST_PATTERN = re.compile(r"notfoo")

    with pytest.raises(
        InvalidArnRestException,
        match="foo is not a valid rest expression for type CustomArn",
    ):
        CustomArn(arn)


@pytest.mark.parametrize(
    "field", ["input_arn", "partition", "service", "region", "account"]
)
def test_cant_use_reserved_field_name(field):
    class CustomArn(Arn):
        REST_PATTERN = re.compile(fr"(?P<{field}>.*)")

    arn = make_arn("service", "rest")
    with pytest.raises(
        ConflictingFieldNamesException,
        match=f"Fields {field} are reserved and cannot be used as field names",
    ):
        CustomArn(arn)
