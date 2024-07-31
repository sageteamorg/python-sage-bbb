Retrieving Current Meetings
===========================

To retrieve a list of all current meetings using the ``python-sage-bbb`` package, follow these steps:

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

4. **Retrieve a list of all current meetings**:

   Use the ``get_meetings`` method to retrieve a list of all current meetings. You can optionally filter the meetings by passing a metadata dictionary.

   .. code-block:: python

      current_meetings = bbb_client.meetings.get_meetings()
      print(f"Current Meetings: {current_meetings}")

This will retrieve a list of all current meetings on your BigBlueButton server.

**Get Meetings Parameters**

The following table lists the parameters you can use when retrieving current meetings:

.. list-table::
   :header-rows: 1

   * - Param Name
     - Type
     - Description
   * - ``metadata``
     - dict
     - A dictionary of metadata to filter the meetings (optional).

For more details on the getMeetings API call, refer to the `BigBlueButton API documentation <https://docs.bigbluebutton.org/development/api/#getMeetings>`_.
