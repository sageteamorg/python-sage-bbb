from typing import Any, Dict
import requests
import logging

logger = logging.getLogger(__name__)


class Configurations:
    """
    This class handles operations related to configurations in BigBlueButton.

    Args:
        client: The client used to interact with the BigBlueButton server.

    Example:
        bbb_client = BigBlueButtonClient(
        "http://example.com/bigbluebutton/api/", "secret"
        )
        configurations = Configurations(bbb_client)
    """

    def __init__(self, client: "BigBlueButtonClient") -> None:
        self.client = client

    def get_default_config_xml(self) -> Dict[str, Any]:
        """
        Retrieves the default configuration XML.

        Returns:
            dict: A dictionary containing the default configuration XML.

        Example:
            configurations = Configurations(bbb_client)
            default_config = configurations.get_default_config_xml()
            print(default_config)
        """
        try:
            logger.info("Attempting to retrieve the default configuration XML.")
            response = self.client.send_request("getDefaultConfigXML")
            logger.info("Successfully retrieved the default configuration XML.")
            return self.client.parse_response(response.content)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.error("Endpoint not found. Please check the API URL and endpoint.")
            else:
                logger.error(f"An HTTP error occurred: {e}")
        except Exception as e:
            logger.error(f"An error occurred while retrieving the default configuration XML: {e}")
        return {}

    def set_config_xml(self, config_xml: str) -> Dict[str, Any]:
        """
        Sets the configuration XML.

        Args:
            config_xml (str): The configuration XML to be set.

        Returns:
            dict: The response from the API call.

        Example:
            configurations = Configurations(bbb_client)
            set_config_response = configurations.set_config_xml("<config>...</config>")
            print(set_config_response)
        """
        try:
            logger.info("Attempting to set the configuration XML.")
            response = self.client.send_request(
                "setConfigXML",
                data=config_xml,
                headers={"Content-Type": "application/xml"},
            )
            logger.info("Successfully set the configuration XML.")
            return self.client.parse_response(response.content)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                logger.error("Endpoint not found. Please check the API URL and endpoint.")
            else:
                logger.error(f"An HTTP error occurred: {e}")
        except Exception as e:
            logger.error(f"An error occurred while setting the configuration XML: {e}")
        return {}
