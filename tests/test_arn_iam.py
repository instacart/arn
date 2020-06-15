from arn.iam import RoleArn

from .conftest import make_arn


def make_iam_arn(rest):
    return make_arn("iam", rest)


def test_parse_iam_role_arn():
    arn = make_iam_arn("role/my-role")
    result = RoleArn(arn)
    assert result.name == "my-role"
