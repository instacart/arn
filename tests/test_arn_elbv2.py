from arn.elbv2 import TargetGroupArn

from .conftest import make_arn


def make_elbv2_arn(rest):
    return make_arn("sts", rest)


def test_parses_target_group():
    arn = make_elbv2_arn("targetgroup/the-tg-name/abcdef0123456789")
    result = TargetGroupArn(arn)
    assert result.name == "the-tg-name"
    assert result.internal_id == "abcdef0123456789"
