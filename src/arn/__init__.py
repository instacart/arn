import re
from dataclasses import dataclass, field
from typing import ClassVar, Match, Pattern, Optional

BASE_PATTERN = re.compile(
    r"^arn:(?P<partition>.+?):(?P<service>.+?):(?P<region>.*?):(?P<account>.+?):(?P<rest>.*)$"
)


class InvalidArnException(Exception):
    def __init__(self, arn: str):
        super().__init__(f"{arn} is not a valid ARN")


class InvalidArnRestException(Exception):
    def __init__(self, rest: str, class_name: str) -> None:
        super().__init__(f"{rest} is not a valid rest expression for type {class_name}")


@dataclass
class Arn:
    REST_PATTERN: ClassVar[Pattern] = re.compile(r"(?P<rest>.*)")

    input_arn: str = ""
    partition: str = ""
    service: str = ""
    region: str = ""
    account: str = ""
    rest: str = field(init=False, default="")

    def __post_init__(self):
        base_match = BASE_PATTERN.match(self.input_arn)
        if not base_match:
            raise InvalidArnException(self.input_arn)
        self._assign_fields_from_match(base_match)

        rest = base_match["rest"]
        rest_match = self.match_rest(rest)
        if not rest_match:
            raise InvalidArnRestException(rest, self.__class__.__name__)
        self.assign_rest(rest_match)

    def match_rest(self, rest: str) -> Optional[Match]:
        return self.REST_PATTERN.match(rest)

    def assign_rest(self, match: Match):
        self._assign_fields_from_match(match)

    def _assign_fields_from_match(self, match):
        if not match:
            raise InvalidArnException(self.input_arn)
        for key in match.re.groupindex.keys():
            if not getattr(self, key):
                setattr(self, key, match[key])
