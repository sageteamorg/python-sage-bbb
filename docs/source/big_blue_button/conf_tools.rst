.. _conf_tools:

Obtaining the Security Salt
===========================

The security salt is a crucial component for interacting with the BigBlueButton API. It is used to generate secure checksums for API requests, ensuring that only authorized users can make changes on the server. If you want to work with ``python-sage-bbb``, you need to obtain your security salt.

To display the current security salt for the BigBlueButton API, you can use the `bbb-conf` command with the `--secret` option. Here’s an example:

.. code-block:: bash

    $ bbb-conf --secret

This command will output the URL and the security salt, like this:

.. code-block:: text

    URL: http://192.168.0.35/bigbluebutton/
    Salt: f6c72afaaae95faa28c3fd90e39e7e6e

Make sure to keep your security salt confidential and secure, as it is essential for authenticating your API requests.

For more details on `bbb-conf` and other configuration tools, please refer to the full documentation: `BigBlueButton Configuration Tools <https://docs.bigbluebutton.org/administration/bbb-conf/>`_.
