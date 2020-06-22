import re
from dataclasses import dataclass, field
from typing import ClassVar, Pattern

from arn import Arn


@dataclass
class TargetGroupArn(Arn):
    REST_PATTERN: ClassVar[Pattern] = re.compile(
        r"targetgroup/(?P<name>.*)/(?P<internal_id>.*)"
    )

    name: str = ""
    internal_id: str = ""
