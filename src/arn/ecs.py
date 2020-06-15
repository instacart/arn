import re
from dataclasses import dataclass, field
from typing import ClassVar, Match, Optional, Pattern

from . import Arn


@dataclass
class TaskDefinitionArn(Arn):
    REST_PATTERN: ClassVar[Pattern] = re.compile(
        r"task-definition/(?P<family>.+):(?P<version>\d+)"
    )

    family: str = field(init=False)
    version: int = field(init=False)

    def assign_rest(self, match: Match):
        super(TaskDefinitionArn, self).assign_rest(match)
        self.version = int(match["version"])


@dataclass
class TaskArn(Arn):
    REST_PATTERN: ClassVar[Pattern] = re.compile(r"task/(?P<id>.+)")

    id: str = field(init=False)


@dataclass
class ServiceArn(Arn):
    rest_pattern_without_cluster: ClassVar[Pattern] = re.compile(
        r"service/(?P<service>.*)"
    )
    rest_pattern_with_cluster: ClassVar[Pattern] = re.compile(
        r"service/(?P<cluster>.*)/(?P<service>.*)"
    )

    cluster: Optional[str] = field(init=False)
    service: str = field(init=False)

    def match_rest(self, rest: str) -> Match:
        match = self.rest_pattern_with_cluster.match(rest)
        if match:
            return match
        match = self.rest_pattern_without_cluster.match(rest)
        if match:
            return match
        return super().match_rest(rest)

    def assign_rest(self, match: Match):
        try:
            self.cluster = match["cluster"]
        except IndexError:
            self.cluster = None
        self.service = match["service"]
