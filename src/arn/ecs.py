import re
from dataclasses import dataclass
from typing import Match

from . import Arn


@dataclass
class ClusterArn(Arn):
    REST_PATTERN = re.compile(r"cluster/(?P<name>.+)")

    name: str = ""


@dataclass
class ContainerInstanceArn(Arn):
    REST_PATTERN = re.compile(r"container-instance/(?P<id>.+)")

    id: str = ""


@dataclass
class ServiceArn(Arn):
    REST_PATTERN_WITHOUT_CLUSTER = re.compile(r"service/(?P<service_name>.*)")
    REST_PATTERN_WITH_CLUSTER = re.compile(
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


@dataclass
class TaskArn(Arn):
    REST_PATTERN = re.compile(r"task/(?P<id>.+)")

    id: str = ""


@dataclass
class TaskDefinitionArn(Arn):
    REST_PATTERN = re.compile(r"task-definition/(?P<family>.+):(?P<version>\d+)")

    family: str = ""
    version: int = 0

    def assign_rest(self, match: Match):
        super(TaskDefinitionArn, self).assign_rest(match)
        self.version = int(match["version"])


@dataclass
class CapacityProviderArn(Arn):
    REST_PATTERN = re.compile(r"capacity-provider/(?P<name>.+)")

    name: str = ""


@dataclass
class TaskSetArn(Arn):
    REST_PATTERN = re.compile(
        r"task-set/(?P<cluster_name>.+)/(?P<service_name>.+)/(?P<id>.+)"
    )

    cluster_name: str = ""
    service_name: str = ""
    id: str = ""
