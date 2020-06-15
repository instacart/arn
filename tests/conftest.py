# Helpers and fixtures go here


def make_arn(
    service: str,
    rest: str,
    partition: str = "aws",
    region: str = "us-east-1",
    account: int = 123456789,
):
    return f"arn:{partition}:{service}:{region}:{account}:{rest}"
