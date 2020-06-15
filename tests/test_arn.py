import pytest

from arn import Arn, InvalidArnException

from .conftest import make_arn


def test_parse_arn_basic():
    arn = make_arn("service", "rest")
    result = Arn(arn)
    assert result.partition == "aws"
    assert result.service == "service"
    assert result.region == "us-east-1"
    assert result.account == 123456789
    assert result.rest == "rest"


@pytest.mark.parametrize("arn", ["arn:aws::::"])
def test_parse_arn_invalid(arn):
    with pytest.raises(InvalidArnException):
        Arn(arn)
