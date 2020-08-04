from __future__ import annotations

import dataclasses
import re
from typing import Any, ClassVar, Match, Optional, Pattern, Set, Union

BASE_PATTERN = re.compile(
    r"^arn:"
    r"(?P<partition>.+?):"
    r"(?P<service>.+?):"
    r"(?P<region>.*?):"
    r"(?P<account>.+?):"
    r"(?P<rest>.*)$"
)


class InvalidArnException(Exception):
    """Raised when the value cannot be parsed as a valid ARN."""

    def __init__(self, arn: str):
        self.arn = arn
        super().__init__(f"{arn} is not a valid ARN")


class InvalidArnRestException(Exception):
    """Raised when the value can be parsed as a valid ARN but the rest cannot."""

    def __init__(self, rest: str, class_name: str) -> None:
        self.rest = rest
        self.class_name = class_name
        super().__init__(f"{rest} is not a valid rest expression for type {class_name}")


class ConflictingFieldNamesException(Exception):
    """A subclass tried to use reserved field names.

    The :py:attr:`partition`, :py:attr:`service`, :py:attr:`region`, and
    :py:attr:`account` names are reserved and cannot be used as attributes.
    """

    def __init__(self, field_names: Set[str]) -> None:
        self.field_names = field_names
        super().__init__(
            f"Fields {', '.join(field_names)} are reserved and "
            f"cannot be used as field names"
        )


@dataclasses.dataclass()
class Arn:
    """The base class that represents an AWS ARN.

    This class is meant to be used as a superclass for more specific ARN classes.
    Instantiating this class with a valid ARN will parse out the common fields
    (:py:attr:`partition`, :py:attr:`service`, :py:attr:`region`, and
    :py:attr:`account`), and will place the rest of the ARN string in the
    :py:attr:`rest` field.
    """

    REST_PATTERN: ClassVar[Union[str, Pattern]] = re.compile(r"(?P<rest>.*)")
    """The pattern that parses the "rest" of the ARN. The "rest" of and ARN is the part
    that is specific to the AWS service that the ARN represents. When overriding in a
    subclass, this value can be either an `re.Pattern`_ or an ``str``.

    .. _re.Pattern: https://docs.python.org/3/library/re.html#regular-expression-objects
    """

    input_arn: Any
    """The instance that was parsed, unchanged."""

    partition: str = ""
    """The partition of the AWS of the resource."""

    service: str = ""
    """The AWS service of the resource."""

    region: str = ""
    """The AWS region in which the resource is located."""

    account: str = ""  # str because some pre-built resources have "aws" as the account
    """The AWS account ID of the resource."""

    rest: str = dataclasses.field(init=False, default="")
    """The rest of the ARN, as matched by :py:const:`REST_PATTERN`."""

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
        """Convert the rest of the ARN into an `re.Match`_.

        By default, matches the rest of the ARN against :py:const:`REST_PATTERN`.
        Override this metod to match against a pattern dynamically. For an example,
        see :py:meth:`arn.ecs.ServiceArn.match_rest`.

        .. _re.Match: https://docs.python.org/3/library/re.html#match-objects
        """
        return re.match(self.REST_PATTERN, rest)

    def assign_rest(self, match: Match):
        """Assign an `re.Match`_'s groups to fields on ``self``.

        By default, assigns all named groups in :py:const:`REST_PATTERN` as strings.
        Override this method to cast group matches to a more appropriate type. For an
        example, see :py:meth:`arn.ecs.TaskDefinitionArn.assign_rest`.

        .. _re.Match: https://docs.python.org/3/library/re.html#match-objects
        """
        self._assign_fields_from_match(match)

    def format_rest(self) -> str:
        """Produce a formatted representation of the rest of the ARN.

        This method is essentially the reverse of :py:meth:`match_rest` and
        :py:meth:`assign_rest`. By default returns :py:data:`rest`. Override this method
        to allow users to override specific fields and get a ``str(...)``
        representation that includes the override.
        """
        return self.rest

    def _assign_fields_from_match(self, match):
        for key in match.re.groupindex.keys():
            if not getattr(self, key):
                setattr(self, key, match[key])
