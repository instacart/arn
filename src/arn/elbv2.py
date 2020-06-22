import re
from dataclasses import dataclass

from arn import Arn


@dataclass
class TargetGroupArn(Arn):
    REST_PATTERN = re.compile(r"targetgroup/(?P<name>.*)/(?P<internal_id>.*)")

    name: str = ""
    internal_id: str = ""
