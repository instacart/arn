"""ARNs for `AWS ECR <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticcontainerregistry.html#amazonelasticcontainerregistry-resources-for-iam-policies>`_."""

import re
from dataclasses import dataclass
from typing import Match

from . import Arn


@dataclass
class RegistryArn(Arn):
    """ARN for an `ECR Registry <https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html>`_."""

    # http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
    #
    # The following regex captures any one of the following ARN formats and
    # appropriately assignes a group name to each part:
    #   - arn:partition:service:region:account-id:resource-id
    #   - arn:partition:service:region:account-id:resource-type/resource-id
    #   - arn:partition:service:region:account-id:resource-type:resource-id
    #
    # Here is a quick, "201" primer to help understand the syntax below:
    #   - (?P<name>...) - Named capture group
    #   - (?:...)       - Non-capturing group
    #
    REST_PATTERN_WITH_OR_WITHOUT_TYPE = re.compile(
        r"(?:(?P<type>[^:\/]+)(?::|\/))?(?P<id>.+)"
    )
    REST_PATTERN_WITHOUT_TYPE = re.compile(r"(?P<id>.+)")
    REST_PATTERN_WITH_TYPE = re.compile(
        r"(?P<type>[^:\/]+)(?::|\/)(?P<id>.+)"
    )

    type: str = ""
    id: str = ""

    def match_rest(self, rest: str) -> Match:
        """
        Overridden to handle `both ARN formats`_.

        Tries to match a new-style ARN with cluster name and falls back to matching
        the ARN without the cluster name.

        .. _both ARN formats: https://www.amazonaws.cn/en/new/2018/amazon-ecs-and-aws-fargate-now-allow-resources-tagging-/
        """
        match = self.REST_PATTERN_WITH_TYPE.match(rest)
        if match:
            return match
        match = self.REST_PATTERN_WITHOUT_TYPE.match(rest)
        if match:
            return match
        return super().match_rest(rest)

    def format_rest(self):
        """
        Overridden to handle `both ARN formats`_.

        If the ARN was originally parsed with the cluster name, it will be added to
        the formatted rest.

        .. _both ARN formats: https://www.amazonaws.cn/en/new/2018/amazon-ecs-and-aws-fargate-now-allow-resources-tagging-/
        """
        if self.type:
            return f"service/{self.cluster}/{self.service_name}"
        else:
            return f"service/{self.service_name}"
