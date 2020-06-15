import re
from dataclasses import dataclass, field
from typing import ClassVar, Pattern

from arn import Arn


@dataclass
class AssumedRoleArn(Arn):
    REST_PATTERN: ClassVar[Pattern] = re.compile(
        r"assumed-role/(?P<role_name>.*)/(?P<role_session_name>.*)"
    )

    role_name: str = field(init=False)
    role_session_name: str = field(init=False)
