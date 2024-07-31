Installing BigBlueButton
========================

To get started with BigBlueButton, you'll need to set up a server. Here's a brief overview of the necessary steps:

1. **Prepare Your Server**: Ensure you have a clean Ubuntu 18.04 64-bit server with at least 4 CPU cores, 8 GB of RAM, and a dedicated SSD with at least 50 GB of free space.

2. **Update Your Server**: Before installing BigBlueButton, update your server with the following commands:

   .. code-block:: bash

      sudo apt-get update
      sudo apt-get dist-upgrade

3. **Install BigBlueButton**: Use the following commands to add the BigBlueButton repository and install the software:

   .. code-block:: bash

      wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash

4. **Configure Firewall**: Make sure to open the necessary ports in your firewall to allow BigBlueButton to operate correctly.

5. **Access BigBlueButton**: Once installed, you can access your BigBlueButton server by navigating to `http://<your-server-ip>` in your web browser.

For a detailed step-by-step guide, including configuration and troubleshooting, please refer to the official BigBlueButton installation documentation: `BigBlueButton Installation Guide <https://docs.bigbluebutton.org/administration/install/>`_.
