Retrieving Detailed Meeting Information
=======================================

To retrieve detailed information about a meeting using the ``python-sage-bbb`` package, follow these steps:

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

4. **Retrieve detailed information about the meeting**:

   Use the ``get_meeting_info`` method to retrieve detailed information about a specific meeting. Provide the meeting ID of the meeting you want to get information about.

   .. code-block:: python

      meeting_info = bbb_client.meetings.get_meeting_info(
          meeting_id="random-9887584"
      )
      print(f"Meeting Info: {meeting_info}")

This will retrieve detailed information about the specified meeting on your BigBlueButton server.

**Get Meeting Info Parameters**

The following table lists the parameters you can use when retrieving detailed meeting information:

.. list-table::
   :header-rows: 1

   * - Param Name
     - Type
     - Description
   * - ``meetingID`` (required)
     - String
     - The meeting ID of the meeting to retrieve information about.

For more details on the getMeetingInfo API call, refer to the `BigBlueButton API documentation <https://docs.bigbluebutton.org/development/api/#getMeetingInfo>`_.
