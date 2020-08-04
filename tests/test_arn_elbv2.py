import pytest

from arn import InvalidArnRestException, elbv2


@pytest.mark.parametrize("lb_type", ["app", "net"])
def test_parses_load_balancer(make_arn, lb_type):
    arn = make_arn("elbv2", f"loadbalancer/{lb_type}/foo/abc123")
    result = elbv2.LoadBalancer(arn)
    assert result.type == lb_type
    assert result.name == "foo"
    assert result.id == "abc123"


def test_rejects_invalid_lb_type(make_arn):
    arn = make_arn("elbv2", f"loadbalancer/notnetorapp/foo/abc123")
    with pytest.raises(InvalidArnRestException):
        elbv2.LoadBalancer(arn)


@pytest.mark.parametrize("lb_type", ["app", "net"])
def test_parses_load_balancer_listener(make_arn, lb_type):
    arn = make_arn("elbv2", f"listener/{lb_type}/foo/abc123/def456")
    result = elbv2.LoadBalancerListener(arn)
    assert result.load_balancer_type == lb_type
    assert result.load_balancer_name == "foo"
    assert result.load_balancer_id == "abc123"
    assert result.listener_id == "def456"


@pytest.mark.parametrize("lb_type", ["app", "net"])
def test_parses_load_balancer_listener_rule(make_arn, lb_type):
    arn = make_arn("elbv2", f"listener-rule/{lb_type}/foo/abc123/def456/789")
    result = elbv2.LoadBalancerListenerRule(arn)
    assert result.load_balancer_type == lb_type
    assert result.load_balancer_name == "foo"
    assert result.load_balancer_id == "abc123"
    assert result.listener_id == "def456"
    assert result.listener_rule_id == "789"


def test_parses_target_group(make_arn):
    arn = make_arn("elbv2", "targetgroup/foo/abcdef0123456789")
    result = elbv2.TargetGroupArn(arn)
    assert result.name == "foo"
    assert result.id == "abcdef0123456789"
