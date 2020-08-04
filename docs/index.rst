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
.. code-block:: python

    from arn.elbv2 import TargetGroupArn

    target_group_arn_str = "arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/foo-bar/abc123"
    target_group_arn = TargetGroupArn(target_group_arn_str)

    # the passed-in str is preserved
    assert target_group_arn.input_arn == target_group_arn_str

    # common attributes
    assert target_group_arn.partition == "aws"
    assert target_group_arn.service == "elasticloadbalancing"
    assert target_group_arn.region == "us-east-1"
    assert target_group_arn.account == "123456789012"

    # attributes specific to the type of AWS resource
    assert target_group_arn.name == "foo-bar"
    assert target_group_arn.id == "abc123"



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   arn

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
