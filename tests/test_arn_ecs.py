from arn import ecs


def test_task_definition(make_arn):
    arn = make_arn("ecs", "task-definition/image:100")
    result = ecs.TaskDefinitionArn(arn)
    assert result.family == "image"
    assert result.version == 100


def test_service_without_cluster(make_arn):
    arn = make_arn("ecs", "service/servicename")
    result = ecs.ServiceArn(arn)
    assert result.cluster == ""
    assert result.service_name == "servicename"


def test_service_with_cluster(make_arn):
    arn = make_arn("ecs", "service/clustername/servicename")
    result = ecs.ServiceArn(arn)
    assert result.cluster == "clustername"
    assert result.service_name == "servicename"


def test_override_cluster(make_arn):
    arn = make_arn("ecs", "service/clustername/servicename")
    result = ecs.ServiceArn(arn, cluster="foo")
    assert result.cluster == "foo"
    assert result.service_name == "servicename"
    assert str(result) == "arn:aws:ecs:us-east-1:123456789:service/foo/servicename"
