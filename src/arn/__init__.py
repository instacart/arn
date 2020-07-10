from __future__ import annotations

import dataclasses
import re
from typing import Any, ClassVar, Match, Optional, Pattern, Set

BASE_PATTERN = re.compile(
    r"^arn:"
    r"(?P<partition>.+?):"
    r"(?P<service>.+?):"
    r"(?P<region>.*?):"
    r"(?P<account>.+?):"
    r"(?P<rest>.*)$"
)


class InvalidArnException(Exception):
    def __init__(self, arn: str):
        super().__init__(f"{arn} is not a valid ARN")


class InvalidArnRestException(Exception):
    def __init__(self, rest: str, class_name: str) -> None:
        super().__init__(f"{rest} is not a valid rest expression for type {class_name}")


class ConflictingFieldNamesException(Exception):
    def __init__(self, field_names: Set[str]) -> None:
        super().__init__(
            f"Fields {', '.join(field_names)} are reserved and "
            f"cannot be used as field names"
        )


@dataclasses.dataclass()
class Arn:
    REST_PATTERN: ClassVar[Pattern] = re.compile(r"(?P<rest>.*)")

    input_arn: Any
    partition: str = ""
    service: str = ""
    region: str = ""
    account: str = ""
    rest: str = dataclasses.field(init=False, default="")

    def __post_init__(self) -> None:
        if isinstance(self.input_arn, bytes):
            arn = self.input_arn.decode()
        elif isinstance(self.input_arn, str):
            arn = self.input_arn
        else:
            arn = str(self.input_arn)

        base_match = BASE_PATTERN.match(arn)
        if not base_match:
            raise InvalidArnException(arn)
        self._assign_fields_from_match(base_match)

        rest = base_match["rest"]
        rest_match = self.match_rest(rest)
        if not rest_match:
            raise InvalidArnRestException(rest, self.__class__.__name__)

        reserved_field_names = {f.name for f in dataclasses.fields(Arn) if f.init}
        subclass_field_names = set(rest_match.re.groupindex.keys())
        conflicting_field_names = reserved_field_names & subclass_field_names
        if conflicting_field_names:
            raise ConflictingFieldNamesException(conflicting_field_names)

        self.assign_rest(rest_match)

    def __str__(self):
        return (
            f"arn:"
            f"{self.partition}:"
            f"{self.service}:"
            f"{self.region}:"
            f"{self.account}:"
            f"{self.format_rest()}"
        )

    def match_rest(self, rest: str) -> Optional[Match]:
        return self.REST_PATTERN.match(rest)

    def assign_rest(self, match: Match):
        self._assign_fields_from_match(match)

    def format_rest(self):
        return self.rest

    def _assign_fields_from_match(self, match):
        for key in match.re.groupindex.keys():
            if not getattr(self, key):
                setattr(self, key, match[key])
