import re
from hashlib import sha1
from typing import Any, Optional
from urllib.parse import quote_plus


class UrlValidator:
    """
    This class provides a method to validate and format the BigBlueButton server base URL.

    Example:
        validated_url = UrlValidator.validate("example.com/bigbluebutton/api/")
        print(validated_url)  # Output: "http://example.com/bigbluebutton/api/"
    """

    @staticmethod
    def validate(bbb_server_base_url: str) -> str:
        """
        Validates and formats the BigBlueButton server base URL.

        Args:
            bbb_server_base_url (str): The base URL of the BigBlueButton server.

        Returns:
            str: The validated and formatted base URL.

        Example:
            validated_url = UrlValidator.validate("example.com/bigbluebutton/api/")
            print(validated_url)  # Output: "http://example.com/bigbluebutton/api/"
        """
        if not re.match(
            r"https?://[a-zA-Z0-9.]+/bigbluebutton/api/", bbb_server_base_url
        ):
            if not bbb_server_base_url.startswith(("http://", "https://")):
                bbb_server_base_url = "http://" + bbb_server_base_url
            if not bbb_server_base_url.endswith("/bigbluebutton/api/"):
                bbb_server_base_url = (
                    bbb_server_base_url[
                        : (
                            bbb_server_base_url.find("/", 8)
                            if bbb_server_base_url.find("/", 8) != -1
                            else len(bbb_server_base_url)
                        )
                    ]
                    + "/bigbluebutton/api/"
                )
        return bbb_server_base_url


class ChecksumStrategy:
    """
    Abstract base class for checksum generation strategies.

    Example:
        class CustomChecksumStrategy(ChecksumStrategy):
            def generate(self, api_call, params, security_salt):
                return "custom_checksum"
    """

    def generate(
        self, api_call: str, params: dict[str, Any], security_salt: str
    ) -> str:
        """
        Generates a checksum for the given API call and parameters.

        Args:
            api_call (str): The API call being made.
            params (dict): The parameters for the API call.
            security_salt (str): The security salt used for generating the checksum.

        Returns:
            str: The generated checksum.

        Example:
            class CustomChecksumStrategy(ChecksumStrategy):
                def generate(self, api_call, params, security_salt):
                    return "custom_checksum"
        """
        raise NotImplementedError(
            "ChecksumStrategy.generate() must be overridden in subclasses"
        )


class DefaultChecksumStrategy(ChecksumStrategy):
    """
    Default implementation of ChecksumStrategy using SHA-1.

    Example:
        checksum_strategy = DefaultChecksumStrategy()
        checksum = checksum_strategy.generate("create", {"meetingID": "123"}, "secret")
        print(checksum)
    """

    def generate(
        self, api_call: str, params: dict[str, Any], security_salt: str
    ) -> str:
        """
        Generates a SHA-1 checksum for the given API call and parameters.

        Args:
            api_call (str): The API call being made.
            params (dict): The parameters for the API call.
            security_salt (str): The security salt used for generating the checksum.

        Returns:
            str: The generated SHA-1 checksum.

        Example:
            checksum_strategy = DefaultChecksumStrategy()
            checksum = checksum_strategy.generate("create",{"meetingID": "123"}, "secret")
            print(checksum)
        """
        secret_str = api_call + self._create_query_string(params) + security_salt
        return sha1(secret_str.encode("utf-8")).hexdigest()

    @staticmethod
    def _convert_value(value: Any) -> str:
        """
        Converts a value to its string representation,
        converting booleans to "true" or "false".

        Args:
            value: The value to convert.

        Returns:
            str: The string representation of the value.

        Example:
            print(DefaultChecksumStrategy._convert_value(True))  # Output: "true"
        """
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    def _create_query_string(self, params: dict[str, Any]) -> str:
        """
        Creates a URL-encoded query string from the given parameters.

        Args:
            params (dict): The parameters to include in the query string.

        Returns:
            str: The URL-encoded query string.

        Example:
            query_string = checksum_strategy._create_query_string({"meetingID": "123"})
            print(query_string)  # Output: "meetingID=123"
        """
        sorted_params = sorted(params.items())
        query_string = "&".join(
            f"{key}={quote_plus(self._convert_value(value))}"
            for key, value in sorted_params
        )
        return query_string


class BigBlueButtonUrlBuilder:
    """
    This class is responsible for building URLs for BigBlueButton API calls.

    Args:
        bbb_server_base_url (str): The base URL of the BigBlueButton server.
        security_salt (str): The security salt used for generating checksums.
        checksum_strategy (ChecksumStrategy, optional):
            The strategy for generating checksums.

    Example:
        url_builder = BigBlueButtonUrlBuilder(
        "http://example.com/bigbluebutton/api/", "secret"
        )
        url = url_builder.build_url("create", {"meetingID": "123"})
        print(url)
    """

    def __init__(
        self,
        bbb_server_base_url: str,
        security_salt: str,
        checksum_strategy: Optional[ChecksumStrategy] = None,
    ) -> None:
        self.bbb_server_base_url = UrlValidator.validate(bbb_server_base_url)
        self.security_salt = security_salt
        self.checksum_strategy = checksum_strategy or DefaultChecksumStrategy()

    def build_url(self, api_call: str, params: Optional[dict[str, Any]] = None) -> str:
        """
        Builds a URL for a BigBlueButton API call.

        Args:
            api_call (str): The API call being made (e.g., "create", "join").
            params (dict): The parameters for the API call.

        Returns:
            str: The complete URL for the API call.

        Example:
            url_builder = BigBlueButtonUrlBuilder(
            "http://example.com/bigbluebutton/api/", "secret"
            )
            url = url_builder.build_url("create", {"meetingID": "123"})
            print(url)
        """
        if params is None:
            params = {}
        params = {
            k: self.checksum_strategy._convert_value(v) for k, v in params.items()
        }
        query_string = self.checksum_strategy._create_query_string(params)
        checksum = self.checksum_strategy.generate(api_call, params, self.security_salt)
        url = f"{self.bbb_server_base_url}{api_call}?{query_string}&checksum={checksum}"
        return url
