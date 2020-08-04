# Helpers and fixtures go here
import pytest


@pytest.fixture(scope="session")
def make_arn():
    def _make_arn(
        service: str,
        rest: str,
        partition: str = "aws",
        region: str = "us-east-1",
        account: int = 123456789,
    ):
        return f"arn:{partition}:{service}:{region}:{account}:{rest}"

    return _make_arn
