from sage_bbb.services.client import BigBlueButtonClient
import time
import requests

# Initialize the client
bbb_client = BigBlueButtonClient(
    "https://live.sageteam.org/bigbluebutton/api/",
    "JvvF6m0ri8khpAQuo7fh7hJI6ifX7Q2nxJ2Ic3CDuU",
)

# Check connection
connection_status = bbb_client.check_connection()
print(f"Connection Status: {connection_status}")

# Create a new meeting with recording enabled
new_meeting = bbb_client.meetings.create_meeting(
    name="Test Meeting",
    meeting_id="random-9887584",
    attendee_pw="ap",
    moderator_pw="mp",
    record=True,  # Enable recording
    # autoStartRecording=True,
    allowStartStopRecording=True
)
print(f"New Meeting: {new_meeting}")

# Join the meeting as a moderator (simulated)
join_url_moderator = bbb_client.meetings.join_meeting(
    meeting=new_meeting,
    full_name="Moderator",
    password=new_meeting.moderator_pw
)
print(f"Join URL (Moderator): {join_url_moderator}")

# Join the meeting as an attendee (simulated)
join_url_attendee = bbb_client.meetings.join_meeting(
    meeting=new_meeting,
    full_name="Attendee",
    password=new_meeting.attendee_pw
)
print(f"Join URL (Attendee): {join_url_attendee}")

# Retrieve a list of all current meetings
current_meetings = bbb_client.meetings.get_meetings()
print(f"Current Meetings: {current_meetings}")

is_running_response = bbb_client.meetings.is_meeting_running(new_meeting)
print(f"Is Meeting Running: {is_running_response}")

# Retrieve detailed information about a specific meeting
meeting_info = bbb_client.meetings.get_meeting_info(new_meeting)
print(f"Meeting Info: {meeting_info}")

# Here you would manually join the meeting using the URLs, start and stop the recording if needed.
# For the purposes of this example, assume the meeting has been recorded.
breakpoint()
# End the meeting
end_meeting_response = bbb_client.meetings.end_meeting(new_meeting)
print(f"End Meeting Response: {end_meeting_response}")
