from arn import s3


def test_parses_access_point_arn(make_arn):
    arn = make_arn("s3", "accesspoint/foo")
    result = s3.AccessPointArn(arn)
    assert result.name == "foo"


def test_parses_bucket_arn(make_arn):
    arn = make_arn("s3", "foo", region='', account='')
    result = s3.BucketArn(arn)
    assert result.name == "foo"


def test_parses_object_arn(make_arn):
    arn = make_arn("s3", "foo/bar", region='', account='')
    result = s3.ObjectArn(arn)
    assert result.bucket_name == "foo"
    assert result.object_name == "bar"


def test_parses_job_arn(make_arn):
    arn = make_arn("s3", "job/foo")
    result = s3.JobArn(arn)
    assert result.id == "foo"
