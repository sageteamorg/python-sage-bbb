from typing import Any, Dict

from sage_bbb.helpers import Meeting


class MeetingFactory:
    @staticmethod
    def create_meeting(response_dict: Dict[str, Any]) -> Meeting:
        """
        Creates a Meeting instance from a response dictionary.

        Args:
            response_dict (dict): The dictionary containing meeting details.

        Returns:
            Meeting: An instance of the Meeting dataclass populated with the
            provided details.

        Example:
            response_dict = {
                "meetingID": "1234",
                "internalMeetingID": "abcd-1234",
                "parentMeetingID": "none",
                "attendeePW": "ap",
                "moderatorPW": "mp",
                "createTime": "1619459200000",
                "voiceBridge": "70000",
                "dialNumber": "123-456-7890",
                "createDate": "2021-04-26T15:00:00Z",
                "hasUserJoined": "true",
                "duration": "60",
                "hasBeenForciblyEnded": "false",
                "messageKey": "welcome",
                "message": "Welcome to the meeting"
            }
            meeting = MeetingFactory.create_meeting(response_dict)
            print(meeting)
        """
        return Meeting(
            meeting_id=response_dict.get("meetingID", ""),
            internal_meeting_id=response_dict.get("internalMeetingID", ""),
            parent_meeting_id=response_dict.get("parentMeetingID", ""),
            attendee_pw=response_dict.get("attendeePW", ""),
            moderator_pw=response_dict.get("moderatorPW", ""),
            create_time=response_dict.get("createTime", ""),
            voice_bridge=response_dict.get("voiceBridge", ""),
            dial_number=response_dict.get("dialNumber", ""),
            create_date=response_dict.get("createDate", ""),
            has_user_joined=response_dict.get("hasUserJoined") == "true",
            duration=int(response_dict.get("duration", 0)),
            has_been_forcibly_ended=response_dict.get("hasBeenForciblyEnded") == "true",
            message_key=response_dict.get("messageKey", ""),
            message=response_dict.get("message", ""),
        )
