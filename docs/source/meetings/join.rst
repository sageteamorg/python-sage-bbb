Joining a Meeting
=================

To join a meeting using the ``python-sage-bbb`` package, follow these steps:

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

4. **Join the meeting as a moderator**:

   Use the ``join_meeting`` method to generate a join URL for a moderator. Replace the `full_name` and `password` parameters with the appropriate values.

   .. code-block:: python

      join_url_moderator = bbb_client.meetings.join_meeting(
          meeting_id="random-9887584",
          full_name="Moderator",
          password="mp"
      )
      print(f"Join URL (Moderator): {join_url_moderator}")

5. **Join the meeting as an attendee**:

   Similarly, use the ``join_meeting`` method to generate a join URL for an attendee. Replace the `full_name` and `password` parameters with the appropriate values.

   .. code-block:: python

      join_url_attendee = bbb_client.meetings.join_meeting(
          meeting_id="random-9887584",
          full_name="Attendee",
          password="ap"
      )
      print(f"Join URL (Attendee): {join_url_attendee}")

This will generate URLs that can be used to join the meeting as either a moderator or an attendee.

**Join Meeting Parameters**

The following table lists the parameters you can use when joining a meeting:

.. list-table::
   :header-rows: 1

   * - Param Name
     - Type
     - Description
   * - ``fullName`` (required)
     - String
     - The full name of the user joining the meeting.
   * - ``meetingID`` (required)
     - String
     - The meeting ID of the meeting to join.
   * - ``password`` (required)
     - String
     - The password for the meeting (either attendee or moderator).
   * - ``createTime``
     - Number
     - The time when the meeting was created.
   * - ``userID``
     - String
     - The user ID of the user joining the meeting.
   * - ``webVoiceConf``
     - String
     - The web voice conference number.
   * - ``configToken``
     - String
     - A token for configuration settings.
   * - ``defaultLayout``
     - String
     - The default layout for the meeting.
   * - ``avatarURL``
     - String
     - The URL of the avatar image for the user.
   * - ``redirect``
     - Boolean
     - Whether to redirect the user after joining.
   * - ``clientURL``
     - String
     - The URL for the client.
   * - ``guest``
     - Boolean
     - Whether the user is joining as a guest.
   * - ``guestStatus``
     - String
     - The status of the guest user.
   * - ``userdata``
     - String
     - Additional user data.

For more details on the join API call, refer to the `BigBlueButton API documentation <https://docs.bigbluebutton.org/development/api/#join>`_.
