import xml.etree.ElementTree as ET
from typing import Any, Dict, Optional

import requests

from sage_bbb.services import Configurations, Meetings, Recordings
from sage_bbb.utils import BigBlueButtonUrlBuilder


class BigBlueButtonClient:
    """
    This class provides a client to interact with a BigBlueButton server.

    Args:
        bbb_server_base_url (str): The base URL of the BigBlueButton server.
        security_salt (str): The security salt used for generating checksums.

    Attributes:
        meetings: An instance of the Meetings class for meeting operations.
        recordings: An instance of the Recordings class for recording operations.
        configurations: An instance of the Configurations class
        for configuration operations.

    Example:
        bbb_client = BigBlueButtonClient(
        "http://example.com/bigbluebutton/api/", "secret"
        )
        connection_status = bbb_client.check_connection()
        print(connection_status)
    """

    def __init__(self, bbb_server_base_url: str, security_salt: str) -> None:
        self.url_builder = BigBlueButtonUrlBuilder(bbb_server_base_url, security_salt)
        self.meetings = Meetings(self)
        self.recordings = Recordings(self)
        self.configurations = Configurations(self)

    def send_request(
        self,
        api_call: str,
        params: Dict[str, Any] = {},
        data: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """
        Sends an HTTP request to the BigBlueButton server.

        Args:
            api_call (str): The API call to be made (e.g., "create", "join").
            params (dict): The parameters to be included in the request.
            data (str, optional): The data to be included in the request body (
            for POST requests
            ).
            headers (dict, optional): The headers to be included in the request.

        Returns:
            requests.Response: The response from the server.

        Example:
            response = self.send_request("getMeetings", params={})
            print(response.content)
        """
        url = self.url_builder.build_url(api_call, params)
        # print(f"Sending request to URL: {url}")
        if data:
            response = requests.post(url, data=data, headers=headers)
        else:
            response = requests.get(url)
        response.raise_for_status()
        return response

    def parse_response(self, response_xml: str) -> Dict[str, Any]:
        """
        Parses the XML response from the server.

        Args:
            response_xml (str): The XML response content.

        Returns:
            dict: A dictionary representation of the XML response.

        Example:
            response_dict = self.parse_response(response.content)
            print(response_dict)
        """
        root = ET.fromstring(response_xml)
        response = {child.tag: child.text for child in root}
        return response

    def check_connection(self) -> Dict[str, Any]:
        """
        Checks the connection to the BigBlueButton server.

        Returns:
            dict: A dictionary containing the response from the server.

        Example:
            connection_status = bbb_client.check_connection()
            print(connection_status)
        """
        response = self.send_request("", {})
        return self.parse_response(response.content)
