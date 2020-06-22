import re
from dataclasses import dataclass

from arn import Arn


@dataclass
class AssumedRoleArn(Arn):
    REST_PATTERN = re.compile(
        r"assumed-role/(?P<role_name>.*)/(?P<role_session_name>.*)"
    )

    role_name: str = ""
    role_session_name: str = ""
