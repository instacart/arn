"""ARNs for `AWS ECS <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticcontainerservice.html#amazonelasticcontainerservice-resources-for-iam-policies>`_."""

import re
from dataclasses import dataclass
from typing import Match

from . import Arn


class NewOldEcsArnMixin:
    def match_rest(self, rest: str) -> Match:
        """
        Overridden to handle `both ARN formats`_.

        Tries to match a new-style ARN with cluster name and falls back to matching
        the ARN without the cluster name.

        .. _both ARN formats: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids
        """
        match = self.REST_PATTERN_WITH_CLUSTER.match(rest)
        if match:
            return match
        match = self.REST_PATTERN_WITHOUT_CLUSTER.match(rest)
        if match:
            return match
        return super().match_rest(rest)


@dataclass
class ClusterArn(Arn):
    """ARN for an `ECS Cluster <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_clusters.html>`_."""

    REST_PATTERN = re.compile(r"cluster/(?P<name>.+)")

    name: str = ""


@dataclass
class ContainerInstanceArn(NewOldEcsArnMixin, Arn):
    """ARN for an `ECS Container Instance <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html>`_."""

    REST_PATTERN_WITHOUT_CLUSTER = re.compile(r"container-instance/(?P<id>.+)")
    REST_PATTERN_WITH_CLUSTER = re.compile(
        r"container-instance/(?P<cluster>.*)/(?P<id>.+)"
    )

    cluster: str = ""
    id: str = ""

    def format_rest(self):
        """
        Overridden to handle `both ARN formats`_.

        If the ARN was originally parsed with the cluster name, it will be added to
        the formatted rest.

        .. _both ARN formats: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids
        """
        if self.cluster:
            return f"container-instance/{self.cluster}/{self.id}"
        else:
            return f"container-instance/{self.id}"


@dataclass
class ServiceArn(NewOldEcsArnMixin, Arn):
    """ARN for an `ECS Service <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`_."""

    REST_PATTERN_WITHOUT_CLUSTER = re.compile(r"service/(?P<service_name>.*)")
    REST_PATTERN_WITH_CLUSTER = re.compile(
        r"service/(?P<cluster>.*)/(?P<service_name>.*)"
    )

    cluster: str = ""
    service_name: str = ""

    def format_rest(self):
        """
        Overridden to handle `both ARN formats`_.

        If the ARN was originally parsed with the cluster name, it will be added to
        the formatted rest.

        .. _both ARN formats: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids
        """
        if self.cluster:
            return f"service/{self.cluster}/{self.service_name}"
        else:
            return f"service/{self.service_name}"


@dataclass
class TaskArn(NewOldEcsArnMixin, Arn):
    """ARN for an `ECS Task <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html>`_."""

    REST_PATTERN_WITHOUT_CLUSTER = re.compile(r"task/(?P<id>.+)")
    REST_PATTERN_WITH_CLUSTER = re.compile(r"task/(?P<cluster>.*)/(?P<id>.+)")

    cluster: str = ""
    id: str = ""

    def format_rest(self):
        """
        Overridden to handle `both ARN formats`_.

        If the ARN was originally parsed with the cluster name, it will be added to
        the formatted rest.

        .. _both ARN formats: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids
        """
        if self.cluster:
            return f"task/{self.cluster}/{self.id}"
        else:
            return f"task/{self.id}"


@dataclass
class TaskDefinitionArn(Arn):
    """ARN for an `ECS Task Definition <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`_."""

    REST_PATTERN = re.compile(r"task-definition/(?P<family>.+):(?P<version>\d+)")

    family: str = ""
    version: int = 0

    def assign_rest(self, match: Match):
        super(TaskDefinitionArn, self).assign_rest(match)
        self.version = int(match["version"])


@dataclass
class CapacityProviderArn(Arn):
    """ARN for an `ECS Capacity Provider <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity_provider_definitions.html>`_."""

    REST_PATTERN = re.compile(r"capacity-provider/(?P<name>.+)")

    name: str = ""


@dataclass
class TaskSetArn(Arn):
    """ARN for an `ECS TaskSet <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_sets.html>`_."""

    REST_PATTERN = re.compile(
        r"task-set/(?P<cluster_name>.+)/(?P<service_name>.+)/(?P<id>.+)"
    )

    cluster_name: str = ""
    service_name: str = ""
    id: str = ""
