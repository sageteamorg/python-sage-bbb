Ending a Meeting
================

To end a meeting using the ``python-sage-bbb`` package, follow these steps:

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

4. **End the meeting**:

   Use the ``end_meeting`` method to end the meeting. Provide the meeting ID and the moderator password of the meeting you want to end.

   .. code-block:: python

      end_meeting_response = bbb_client.meetings.end_meeting(
          meeting_id="random-9887584",
          moderator_pw="mp"
      )
      print(f"End Meeting Response: {end_meeting_response}")

This will end the specified meeting on your BigBlueButton server.

**End Meeting Parameters**

The following table lists the parameters you can use when ending a meeting:

.. list-table::
   :header-rows: 1

   * - Param Name
     - Type
     - Description
   * - ``meetingID`` (required)
     - String
     - The meeting ID of the meeting to end.
   * - ``password`` (required)
     - String
     - The password for the meeting (usually the moderator password).

For more details on the end API call, refer to the `BigBlueButton API documentation <https://docs.bigbluebutton.org/development/api/#end>`_.
