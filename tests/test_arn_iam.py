import pytest

from arn import InvalidArnException, iam


def test_parse_iam_role_arn(make_arn):
    arn = make_arn("iam", "role/my-role")
    result = iam.RoleArn(arn)
    assert result.name == "my-role"


def test_parses_assumed_role(make_arn):
    arn = make_arn("sts", "assumed-role/my-task-role/test")
    result = iam.AssumedRoleArn(arn)
    assert result.role_name == "my-task-role"
    assert result.role_session_name == "test"


def test_rejects_not_assumed_role(make_arn):
    not_an_arn = "foo"
    with pytest.raises(InvalidArnException, match=not_an_arn):
        iam.AssumedRoleArn(not_an_arn)
