Welcome to arn's documentation!
===============================

A Python library for parsing `AWS ARNs <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_.


Installation
^^^^^^^^^^^^

To install, just run

.. code-block:: bash

    pip install arn

or add the library to your ``setup.py`` / ``requirements.txt``.

Basic Usage
^^^^^^^^^^^

To parse an ARN string, use the class that corresponds to the type of ARN. The properties of the ARN are available as members on the result:

.. code-block:: python

    from arn.elbv2 import TargetGroupArn

    target_group_arn_str = "arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/foo-bar/abc123"
    target_group_arn = TargetGroupArn(target_group_arn_str)

    # use the ARN instance's __str__ to format the ARN back into a string
    assert str(target_group_arn) == target_group_arn_str

    # common attributes
    assert target_group_arn.partition == "aws"
    assert target_group_arn.service == "elasticloadbalancing"
    assert target_group_arn.region == "us-east-1"
    assert target_group_arn.account == "123456789012"

    # attributes specific to the type of AWS resource
    assert target_group_arn.name == "foo-bar"
    assert target_group_arn.id == "abc123"

The full list of supported ARNs is available here:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   arn

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
