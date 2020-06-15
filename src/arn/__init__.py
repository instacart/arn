import re
from dataclasses import dataclass, field
from typing import ClassVar, Match, Pattern

BASE_PATTERN = re.compile(
    r"^arn:(?P<partition>.+?):(?P<service>.+?):(?P<region>.*?):(?P<account>\d*?):(?P<rest>.*)$"
)


class InvalidArnException(Exception):
    def __init__(self, arn):
        super().__init__(f"{arn} is not a valid ARN")


@dataclass
class Arn:
    REST_PATTERN: ClassVar[Pattern] = re.compile(r"(?P<rest>.*)")

    arn: str = field(repr=False)
    partition: str = field(init=False)
    service: str = field(init=False)
    region: str = field(init=False)
    account: int = field(init=False)
    rest: str = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        match = BASE_PATTERN.match(self.arn)
        if not match:
            raise InvalidArnException(self.arn)

        self.partition = match["partition"]
        self.service = match["service"]
        self.region = match["region"]
        self.account = int(match["account"])
        self.assign_rest(self.match_rest(match["rest"]))

    def match_rest(self, rest: str) -> Match:
        rest_match = self.REST_PATTERN.match(rest)
        if not rest_match:
            raise InvalidArnException(self.arn)
        return rest_match

    def assign_rest(self, match: Match):
        for key in match.re.groupindex.keys():
            setattr(self, key, match[key])
