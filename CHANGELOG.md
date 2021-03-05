# Changelog

## v0.1.5
- Fixed support for Python 3.6
- Added support for the new-style ECS ARN to `ContainerInstance` and `Task`

## v0.1.4 - Make account optional
`account` is now an optional field, to handle resources that are cross-account such as S3 buckets (#9, thanks @ikben)

## v0.1.3 Another docs update
Made the version in the Sphinx config the same as the wheel version

## v0.1.2 - Docs update
No changes, just updated the description in setup.py

## v0.1.0 - Initial public release
Initial public release, with support for the following ARNs:

- ECS
  - Capacity provider
  - Container Instance
  - Cluster
  - Service
  - Task
  - Task definition
  - TaskSet
- ELBv2
  - Load Balancers (Application and Network)
  - ALB/NLB Listeners
  - ALB/NLB Listener Rules
  - Target Group
- IAM
  - Role
  - STS Assumed role
- S3
  - Access point
  - Bucket
  - Job
  - Object
