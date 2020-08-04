"""ARNs for `AWS S3 <https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies>`_."""

import re

from arn import Arn


class AccessPointArn(Arn):
    """ARN for an `S3 Access Point <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html>`_."""

    REST_PATTERN = re.compile(r"accesspoint/(?P<name>.*)")

    name: str = ""


class BucketArn(Arn):
    """ARN for an `S3 Bucket <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html>`_."""

    REST_PATTERN = re.compile(r"(?P<name>.*)")

    name: str = ""


class ObjectArn(Arn):
    """ARN for an `S3 Object <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html>`_."""

    REST_PATTERN = re.compile(r"(?P<bucket_name>.*)/(?P<object_name>.*)")

    bucket_name: str = ""
    object_name: str = ""


class JobArn(Arn):
    """ARN for an `S3 Batch Job <https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html>`_."""

    REST_PATTERN = re.compile(r"job/(?P<id>.*)")

    id: str = ""
