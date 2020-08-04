"""ARNs for `AWS IAM <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_identityandaccessmanagement.html#identityandaccessmanagement-resources-for-iam-policiess>`_."""

import re
from dataclasses import dataclass

from . import Arn


@dataclass
class RoleArn(Arn):
    """ARN for an `IAM Role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_."""

    REST_PATTERN = re.compile(r"role/(?P<name>.*)")

    name: str = ""


@dataclass
class AssumedRoleArn(Arn):
    """ARN for an `IAM Assumed Role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html>`_."""

    REST_PATTERN = re.compile(
        r"assumed-role/(?P<role_name>.*)/(?P<role_session_name>.*)"
    )

    role_name: str = ""
    role_session_name: str = ""
