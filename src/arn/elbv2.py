import re
from dataclasses import dataclass

from arn import Arn


@dataclass
class ApplicationLoadBalancer(Arn):
    REST_PATTERN = re.compile(r"loadbalancer/app/(?P<name>.*)/(?P<id>.*)")

    name: str = ""
    id: str = ""


@dataclass
class ApplicationLoadBalancerListener(Arn):
    REST_PATTERN = re.compile(
        r"listener/app/(?P<load_balancer_name>.*)/(?P<load_balancer_id>.*)"
        r"/(?P<listener_id>.*)"
    )

    load_balancer_name: str = ""
    load_balancer_id: str = ""
    listener_id: str = ""


@dataclass
class TargetGroupArn(Arn):
    REST_PATTERN = re.compile(r"targetgroup/(?P<name>.*)/(?P<id>.*)")

    name: str = ""
    id: str = ""
