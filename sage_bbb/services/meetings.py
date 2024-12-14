from typing import Any, Dict, Optional
import logging

from sage_bbb.services.factory import MeetingFactory

logger = logging.getLogger(__name__)


class Meetings:
    """
    This class handles operations related to meetings in BigBlueButton.

    Args:
        client: The client used to interact with the BigBlueButton server.

    Example:
        bbb_client = BigBlueButtonClient(
        "http://example.com/bigbluebutton/api/", "secret"
        )
        meetings = Meetings(bbb_client)
    """

    def __init__(self, client: "BigBlueButtonClient") -> None:
        self.client = client

    def get_meetings(self, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves a list of all current meetings, optionally filtered by metadata.

        Args:
            metadata (dict, optional): A dictionary of metadata to filter the meetings.

        Returns:
            dict: A dictionary containing information about the current meetings.

        Example:
            meetings = Meetings(bbb_client)
            current_meetings = meetings.get_meetings()
            print(current_meetings)

            filtered_meetings = meetings.get_meetings({"title": "Test Meeting"})
            print(filtered_meetings)
        """
        params = metadata if metadata else {}
        logger.info("Retrieving meetings with params: %s", params)
        response = self.client.send_request("getMeetings", params)
        logger.info("Meetings retrieved successfully.")
        return self.client.parse_response(response.content)

    def create_meeting(
        self,
        name: str,
        meeting_id: str,
        attendee_pw: str,
        moderator_pw: str,
        **kwargs: Any,
    ) -> "Meeting":
        """
        Creates a new meeting.

        Args:
            name (str): The name of the meeting.
            meeting_id (str): The unique identifier for the meeting.
            attendee_pw (str): The password for attendees.
            moderator_pw (str): The password for moderators.
            **kwargs: Additional optional parameters for the meeting.

        Returns:
            Meeting: An instance of the Meeting dataclass
            containing details about the created meeting.

        Example:
            meetings = Meetings(bbb_client)
            new_meeting = meetings.create_meeting(
                name="Test Meeting",
                meeting_id="1234",
                attendee_pw="ap",
                moderator_pw="mp"
            )
            print(new_meeting)
        """
        params = {
            "name": name,
            "meetingID": meeting_id,
            "attendeePW": attendee_pw,
            "moderatorPW": moderator_pw,
            **kwargs,
        }
        logger.info("Creating meeting with params: %s", params)
        response = self.client.send_request("create", params)
        response_dict = self.client.parse_response(response.content)
        logger.info("Meeting created successfully with ID: %s", meeting_id)
        return MeetingFactory.create_meeting(response_dict)

    def join_meeting(
        self, meeting_id: str, full_name: str, password: str, **kwargs: Any
    ) -> str:
        """
        Constructs the URL for joining a meeting.

        Args:
            meeting_id (str): The unique identifier for the meeting.
            full_name (str): The full name of the user joining the meeting.
            password (str): The password for the meeting (attendee or moderator).
            **kwargs: Additional optional parameters for the join URL.

        Returns:
            str: The URL for joining the meeting.

        Example:
            join_url = meetings.join_meeting(
                meeting_id="1234",
                full_name="John Doe",
                password="ap"
            )
            print(join_url)
        """
        params = {
            "fullName": full_name,
            "meetingID": meeting_id,
            "password": password,
            **kwargs,
        }
        logger.info("Joining meeting ID: %s with full name: %s", meeting_id, full_name)
        join_url = self.client.url_builder.build_url("join", params)
        logger.info("Join URL generated: %s", join_url)
        return join_url

    def end_meeting(self, meeting_id: str, moderator_pw: str) -> Dict[str, Any]:
        """
        Ends a meeting.

        Args:
            meeting_id (str): The unique identifier for the meeting.
            moderator_pw (str): The password for moderators.

        Returns:
            dict: The response from the API call.

        Example:
            end_meeting_response = meetings.end_meeting("1234", "mp")
            print(end_meeting_response)
        """
        params = {
            "meetingID": meeting_id,
            "password": moderator_pw,
        }
        logger.info("Ending meeting ID: %s", meeting_id)
        response = self.client.send_request("end", params)
        logger.info("Meeting ID %s ended successfully.", meeting_id)
        return self.client.parse_response(response.content)

    def is_meeting_running(self, meeting_id: str) -> Dict[str, Any]:
        """
        Checks if a meeting is currently running.

        Args:
            meeting_id (str): The unique identifier for the meeting.

        Returns:
            dict: The response from the API call.

        Example:
            is_running_response = meetings.is_meeting_running("1234")
            print(is_running_response)
        """
        params = {
            "meetingID": meeting_id,
        }
        logger.info("Checking if meeting ID: %s is running.", meeting_id)
        response = self.client.send_request("isMeetingRunning", params)
        logger.info("Meeting running status retrieved for meeting ID: %s", meeting_id)
        return self.client.parse_response(response.content)

    def get_meeting_info(self, meeting_id: str) -> Dict[str, Any]:
        """
        Retrieves detailed information about a meeting.

        Args:
            meeting_id (str): The unique identifier for the meeting.

        Returns:
            dict: The response from the API call.

        Example:
            meeting_info = meetings.get_meeting_info("1234")
            print(meeting_info)
        """
        params = {
            "meetingID": meeting_id,
        }
        logger.info("Retrieving information for meeting ID: %s", meeting_id)
        response = self.client.send_request("getMeetingInfo", params)
        logger.info("Meeting information retrieved for meeting ID: %s", meeting_id)
        return self.client.parse_response(response.content)
