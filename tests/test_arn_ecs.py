from arn import ecs


def test_cluster(make_arn):
    arn = make_arn("ecs", "cluster/foo")
    result = ecs.ClusterArn(arn)
    assert result.name == "foo"


def test_container_instance_without_cluster(make_arn):
    arn = make_arn("ecs", "container-instance/abc123")
    result = ecs.ContainerInstanceArn(arn)
    assert result.cluster == ""
    assert result.id == "abc123"


def test_container_instance_with_cluster(make_arn):
    arn = make_arn("ecs", "container-instance/foo/abc123")
    result = ecs.ContainerInstanceArn(arn)
    assert result.cluster == "foo"
    assert result.id == "abc123"


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


def test_service_override_cluster(make_arn):
    arn = make_arn("ecs", "service/clustername/servicename")
    result = ecs.ServiceArn(arn, cluster="foo")
    assert result.cluster == "foo"
    assert result.service_name == "servicename"
    assert str(result) == "arn:aws:ecs:us-east-1:123456789:service/foo/servicename"


def test_task_without_cluster(make_arn):
    arn = make_arn("ecs", "task/abc123")
    result = ecs.TaskArn(arn)
    assert result.cluster == ""
    assert result.id == "abc123"


def test_task_with_cluster(make_arn):
    arn = make_arn("ecs", "task/foo/abc123")
    result = ecs.TaskArn(arn)
    assert result.cluster == "foo"
    assert result.id == "abc123"


def test_task_definition(make_arn):
    arn = make_arn("ecs", "task-definition/image:100")
    result = ecs.TaskDefinitionArn(arn)
    assert result.family == "image"
    assert result.version == 100


def test_capacity_provider(make_arn):
    arn = make_arn("ecs", "capacity-provider/foo")
    result = ecs.CapacityProviderArn(arn)
    assert result.name == "foo"


def test_task_set(make_arn):
    arn = make_arn("ecs", "task-set/foo/bar/abc123")
    result = ecs.TaskSetArn(arn)
    assert result.cluster_name == "foo"
    assert result.service_name == "bar"
    assert result.id == "abc123"
