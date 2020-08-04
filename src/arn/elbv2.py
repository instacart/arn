import re
from dataclasses import dataclass

from arn import Arn


@dataclass
class LoadBalancer(Arn):
    REST_PATTERN = re.compile(r"loadbalancer/(?P<type>app|net)/(?P<name>.*)/(?P<id>.*)")

    type: str = ""
    name: str = ""
    id: str = ""


@dataclass
class LoadBalancerListener(Arn):
    REST_PATTERN = re.compile(
        r"listener/(?P<load_balancer_type>app|net)/(?P<load_balancer_name>.*)"
        r"/(?P<load_balancer_id>.*)/(?P<listener_id>.*)"
    )

    load_balancer_type: str = ""
    load_balancer_name: str = ""
    load_balancer_id: str = ""
    listener_id: str = ""


@dataclass
class LoadBalancerListenerRule(Arn):
    REST_PATTERN = re.compile(
        r"listener-rule/(?P<load_balancer_type>app|net)/(?P<load_balancer_name>.*)"
        r"/(?P<load_balancer_id>.*)/(?P<listener_id>.*)/(?P<listener_rule_id>.*)"
    )

    load_balancer_type: str = ""
    load_balancer_name: str = ""
    load_balancer_id: str = ""
    listener_id: str = ""
    listener_rule_id: str = ""


@dataclass
class TargetGroupArn(Arn):
    REST_PATTERN = re.compile(r"targetgroup/(?P<name>.*)/(?P<id>.*)")

    name: str = ""
    id: str = ""
