import re
from dataclasses import dataclass, field
from typing import ClassVar, Pattern

from . import Arn


@dataclass
class RoleArn(Arn):
    REST_PATTERN: ClassVar[Pattern] = re.compile(r"role/(?P<name>.*)")

    name: str = field(init=False)
