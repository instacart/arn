"""ARNS for `AWS RDS <https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonrds.html#amazonrds-resources-for-iam-policies>`_."""

import re

from arn import Arn


@dataclass
class RdsDbArn(Arn):
    REST_PATTERN = re.compile(r"db:(?P<name>.+)")
    name: str = ""


@dataclass
class RdsSnapshotArn(Arn):
    REST_PATTERN = re.compile(r"snapshot:(?P<name>.+)")

    name: str = ""
