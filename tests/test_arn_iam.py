from arn.iam import RoleArn


def test_parse_iam_role_arn(make_arn):
    arn = make_arn("iam", "role/my-role")
    result = RoleArn(arn)
    assert result.name == "my-role"
