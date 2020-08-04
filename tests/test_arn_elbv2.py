from arn.elbv2 import TargetGroupArn


def test_parses_target_group(make_arn):
    arn = make_arn("elbv2", "targetgroup/the-tg-name/abcdef0123456789")
    result = TargetGroupArn(arn)
    assert result.name == "the-tg-name"
    assert result.internal_id == "abcdef0123456789"
