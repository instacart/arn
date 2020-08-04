import re

from arn import Arn


class AccessPointArn(Arn):
    REST_PATTERN = re.compile(r"accesspoint/(?P<name>.*)")

    name: str = ""


class BucketArn(Arn):
    REST_PATTERN = re.compile(r"(?P<name>.*)")

    name: str = ""


class ObjectArn(Arn):
    REST_PATTERN = re.compile(r"(?P<bucket_name>.*)/(?P<object_name>.*)")

    bucket_name: str = ""
    object_name: str = ""


class JobArn(Arn):
    REST_PATTERN = re.compile(r"job/(?P<id>.*)")

    id: str = ""
