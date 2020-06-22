from arn import ecs

from .conftest import make_arn


def make_ecs_arn(rest):
    return make_arn("ecs", rest)


def test_task_definition():
    arn = make_ecs_arn("task-definition/image:100")
    result = ecs.TaskDefinitionArn(arn)
    assert result.family == "image"
    assert result.version == 100


def test_service_without_cluster():
    arn = make_ecs_arn("service/servicename")
    result = ecs.ServiceArn(arn)
    assert result.cluster == ""
    assert result.service == "servicename"


def test_service_with_cluster():
    arn = make_ecs_arn("service/clustername/servicename")
    result = ecs.ServiceArn(arn)
    assert result.cluster == "clustername"
    assert result.service == "servicename"
