Checking if a Meeting is Running
================================

To check if a meeting is currently running using the ``python-sage-bbb`` package, follow these steps:

1. **Import the necessary modules**:

   .. code-block:: python

      from sage_bbb.services.client import BigBlueButtonClient

2. **Initialize the client**:

   Initialize the client with your BigBlueButton server URL and security salt. Replace the placeholder values with your actual server URL and security salt.

   .. code-block:: python

      bbb_client = BigBlueButtonClient(
          "http://your-bbb-server.com/bigbluebutton/api/",
          "your-security-salt",
      )

3. **Create a new meeting**:

   If you haven't already created a meeting, use the ``create_meeting`` method to do so.

   .. code-block:: python

      new_meeting = bbb_client.meetings.create_meeting(
          name="Test Meeting",
          meeting_id="random-9887584",
          attendee_pw="ap",
          moderator_pw="mp",
          record=True,  # Enable recording
          allowStartStopRecording=True
      )
      print(f"New Meeting: {new_meeting}")

4. **Check if the meeting is running**:

   Use the ``is_meeting_running`` method to check if a meeting is currently running. Provide the meeting ID of the meeting you want to check.

   .. code-block:: python

      is_running_response = bbb_client.meetings.is_meeting_running(
          meeting_id="random-9887584"
      )
      print(f"Is Meeting Running: {is_running_response}")

This will check if the specified meeting is currently running on your BigBlueButton server.

**Is Meeting Running Parameters**

The following table lists the parameters you can use when checking if a meeting is running:

.. list-table::
   :header-rows: 1

   * - Param Name
     - Type
     - Description
   * - ``meetingID`` (required)
     - String
     - The meeting ID of the meeting to check.

For more details on the isMeetingRunning API call, refer to the `BigBlueButton API documentation <https://docs.bigbluebutton.org/development/api/#isMeetingRunning>`_.
