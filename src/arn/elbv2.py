"""ARNs for `AWS ELBv2 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_elasticloadbalancingv2.html#elasticloadbalancingv2-resources-for-iam-policies>`_.

.. _ALB: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html#application-load-balancer-overview
.. _NLB: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html#network-load-balancer-overview
"""

import re
from dataclasses import dataclass

from arn import Arn


@dataclass
class LoadBalancer(Arn):
    """ARN for an `ALB`_ and `NLB`_."""

    REST_PATTERN = re.compile(r"loadbalancer/(?P<type>app|net)/(?P<name>.*)/(?P<id>.*)")

    type: str = ""
    """The type of load balancer, ``app`` for Application, ``net`` for Network."""

    name: str = ""
    id: str = ""


@dataclass
class LoadBalancerListener(Arn):
    """ARN for `ALB`_ and `NLB`_ listeners."""

    REST_PATTERN = re.compile(
        r"listener/(?P<load_balancer_type>app|net)/(?P<load_balancer_name>.*)"
        r"/(?P<load_balancer_id>.*)/(?P<listener_id>.*)"
    )

    load_balancer_type: str = ""
    """The type of load balancer, ``app`` for Application, ``net`` for Network."""

    load_balancer_name: str = ""
    load_balancer_id: str = ""
    listener_id: str = ""


@dataclass
class LoadBalancerListenerRule(Arn):
    """ARN for `ALB`_ and `NLB`_ listener rules."""

    REST_PATTERN = re.compile(
        r"listener-rule/(?P<load_balancer_type>app|net)/(?P<load_balancer_name>.*)"
        r"/(?P<load_balancer_id>.*)/(?P<listener_id>.*)/(?P<listener_rule_id>.*)"
    )

    load_balancer_type: str = ""
    """The type of load balancer, ``app`` for Application, ``net`` for Network."""

    load_balancer_name: str = ""
    load_balancer_id: str = ""
    listener_id: str = ""
    listener_rule_id: str = ""


@dataclass
class TargetGroupArn(Arn):
    """ARN for a `Target Group <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html>`_."""

    REST_PATTERN = re.compile(r"targetgroup/(?P<name>.*)/(?P<id>.*)")

    name: str = ""
    id: str = ""
