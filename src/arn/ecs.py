import re
from dataclasses import dataclass, field
from typing import ClassVar, Match, Optional, Pattern

from . import Arn


@dataclass
class TaskDefinitionArn(Arn):
    REST_PATTERN: ClassVar[Pattern] = re.compile(
        r"task-definition/(?P<family>.+):(?P<version>\d+)"
    )

    family: str = ""
    version: int = 0

    def assign_rest(self, match: Match):
        super(TaskDefinitionArn, self).assign_rest(match)
        self.version = int(match["version"])


@dataclass
class TaskArn(Arn):
    REST_PATTERN: ClassVar[Pattern] = re.compile(r"task/(?P<id>.+)")

    id: str = ""


@dataclass
class ServiceArn(Arn):
    REST_PATTERN_WITHOUT_CLUSTER: ClassVar[Pattern] = re.compile(
        r"service/(?P<service_name>.*)"
    )
    REST_PATTERN_WITH_CLUSTER: ClassVar[Pattern] = re.compile(
        r"service/(?P<cluster>.*)/(?P<service_name>.*)"
    )

    cluster: str = ""
    service_name: str = ""

    def match_rest(self, rest: str) -> Match:
        match = self.REST_PATTERN_WITH_CLUSTER.match(rest)
        if match:
            return match
        match = self.REST_PATTERN_WITHOUT_CLUSTER.match(rest)
        if match:
            return match
        return super().match_rest(rest)

    def format_rest(self):
        if self.cluster:
            return f"service/{self.cluster}/{self.service_name}"
        else:
            return f"service/{self.service_name}"
