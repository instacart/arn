import re
from dataclasses import dataclass

from . import Arn


@dataclass
class RoleArn(Arn):
    REST_PATTERN = re.compile(r"role/(?P<name>.*)")

    name: str = ""
