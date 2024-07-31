from dataclasses import dataclass


@dataclass
class Meeting:
    meeting_id: str
    internal_meeting_id: str
    parent_meeting_id: str
    attendee_pw: str
    moderator_pw: str
    create_time: str
    voice_bridge: str
    dial_number: str
    create_date: str
    has_user_joined: bool
    duration: int
    has_been_forcibly_ended: bool
    message_key: str
    message: str
