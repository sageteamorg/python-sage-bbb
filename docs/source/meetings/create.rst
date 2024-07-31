Creating a Meeting
==================

To create a meeting using the ``python-sage-bbb`` package, follow these steps:

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

3. **Check the connection**:

   Before creating a meeting, you can check the connection to ensure everything is set up correctly.

   .. code-block:: python

      connection_status = bbb_client.check_connection()
      print(f"Connection Status: {connection_status}")

4. **Create a new meeting**:

   Use the ``create_meeting`` method to create a new meeting. You can specify various parameters such as the meeting name, meeting ID, attendee and moderator passwords, and whether to enable recording.

   .. code-block:: python

      new_meeting = bbb_client.meetings.create_meeting(
          name="Test Meeting",
          meeting_id="random-9887584",
          attendee_pw="ap",
          moderator_pw="mp",
          record=True,  # Enable recording
          autoStartRecording=True,
          allowStartStopRecording=True
      )
      print(f"New Meeting: {new_meeting}")

This will create a new meeting on your BigBlueButton server. You can customize the meeting by passing additional parameters as described in the BigBlueButton API documentation.

**Create Meeting Parameters**

The following table lists the parameters you can use when creating a meeting:

.. list-table::
   :header-rows: 1

   * - Param Name
     - Type
     - Description
   * - ``name`` (required)
     - String
     - A name for the meeting.
   * - ``meetingID`` (required)
     - String
     - A meeting ID that can be used to identify this meeting by the 3rd-party application. Must be unique.
   * - ``attendeePW``
     - String
     - [DEPRECATED] The password for attendees.
   * - ``moderatorPW``
     - String
     - [DEPRECATED] The password for moderators.
   * - ``welcome``
     - String
     - A welcome message that gets displayed on the chat window when the participant joins.
   * - ``dialNumber``
     - String
     - The dial access number that participants can call in using regular phone.
   * - ``voiceBridge``
     - String
     - Voice conference number for the FreeSWITCH voice conference associated with this meeting.
   * - ``maxParticipants``
     - Number
     - The maximum number of users allowed to join the conference at the same time.
   * - ``logoutURL``
     - String
     - The URL that the BigBlueButton client will go to after users click the OK button on the ‘You have been logged out’ message.
   * - ``record``
     - Boolean
     - Setting ‘record=true’ instructs the BigBlueButton server to record the media and events in the session for later playback.
   * - ``duration``
     - Number
     - The maximum length (in minutes) for the meeting.
   * - ``isBreakout``
     - Boolean
     - Must be set to true to create a breakout room.
   * - ``parentMeetingID``
     - String
     - Must be provided when creating a breakout room.
   * - ``sequence``
     - Number
     - The sequence number of the breakout room.
   * - ``freeJoin``
     - Boolean
     - If set to true, the client will give the user the choice to choose the breakout rooms they want to join.
   * - ``meta``
     - String
     - Pass one or more metadata values when creating a meeting.
   * - ``moderatorOnlyMessage``
     - String
     - Display a message to all moderators in the public chat.
   * - ``autoStartRecording``
     - Boolean
     - Automatically start recording when the first user joins.
   * - ``allowStartStopRecording``
     - Boolean
     - Allow the user to start/stop recording.
   * - ``webcamsOnlyForModerator``
     - Boolean
     - Setting webcamsOnlyForModerator=true will cause all webcams shared by viewers to only appear for moderators.
   * - ``bannerText``
     - String
     - Set the banner text in the client.
   * - ``bannerColor``
     - String
     - Set the banner background color in the client.
   * - ``muteOnStart``
     - Boolean
     - Setting true will mute all users when the meeting starts.
   * - ``allowModsToUnmuteUsers``
     - Boolean
     - Allow moderators to unmute other users in the meeting.
   * - ``lockSettingsDisableCam``
     - Boolean
     - Prevent users from sharing their camera in the meeting.
   * - ``lockSettingsDisableMic``
     - Boolean
     - Only allow users to join in listen-only mode.
   * - ``lockSettingsDisablePrivateChat``
     - Boolean
     - Disable private chats in the meeting.
   * - ``lockSettingsDisablePublicChat``
     - Boolean
     - Disable public chat in the meeting.
   * - ``lockSettingsDisableNotes``
     - Boolean
     - Disable notes in the meeting.
   * - ``lockSettingsHideUserList``
     - Boolean
     - Prevent viewers from seeing other viewers in the user list.
   * - ``lockSettingsLockOnJoin``
     - Boolean
     - Apply lock settings to users when they join.
   * - ``lockSettingsHideViewersCursor``
     - Boolean
     - Prevent viewers from seeing other viewers' cursor when multi-user whiteboard is on.
   * - ``guestPolicy``
     - Enum
     - Set the guest policy for the meeting.
   * - ``endWhenNoModerator``
     - Boolean
     - Automatically end the meeting when no moderators are present.
   * - ``meetingLayout``
     - Enum
     - Set the default layout for the meeting.
   * - ``learningDashboardEnabled``
     - Boolean
     - Enable the Learning Dashboard for the meeting.
   * - ``allowModsToEjectCameras``
     - Boolean
     - Allow moderators to close other users' cameras.
   * - ``allowRequestsWithoutSession``
     - Boolean
     - Allow users to join meetings without session cookie validation.
   * - ``virtualBackgroundsDisabled``
     - Boolean
     - Disable virtual backgrounds for all users in the meeting.
   * - ``userCameraCap``
     - Number
     - Defines the max number of webcams a single user can share simultaneously.
   * - ``meetingCameraCap``
     - Number
     - Defines the max number of webcams a meeting can have simultaneously.
   * - ``meetingExpireIfNoUserJoinedInMinutes``
     - Number
     - Automatically end meeting if no user joins within a specified period after meeting creation.
   * - ``meetingExpireWhenLastUserLeftInMinutes``
     - Number
     - Automatically end meeting a specified number of minutes after the last user leaves.
   * - ``groups``
     - String
     - Pre-defined groups to automatically assign students to breakout rooms.
   * - ``logo``
     - String
     - URL to an image displayed above the participants list.
   * - ``disabledFeatures``
     - String
     - Comma-separated list of features to disable in a meeting.
   * - ``disabledFeaturesExclude``
     - String
     - Comma-separated list of features to exclude from being disabled.
   * - ``preUploadedPresentationOverrideDefault``
     - Boolean
     - Whether to override the default presentation with a pre-uploaded presentation.
   * - ``notifyRecordingIsOn``
     - Boolean
     - Display a modal to collect recording consent from users when recording starts.
   * - ``presentationUploadExternalUrl``
     - String
     - URL to an external application for uploading presentation files.
   * - ``presentationUploadExternalDescription``
     - String
     - Description of how to use an external application to upload presentation files.
   * - ``recordFullDurationMedia``
     - Boolean
     - Capture media for the full duration of the meeting if recording is enabled.
   * - ``preUploadedPresentation``
     - String
     - URL to a pre-uploaded presentation file.
   * - ``preUploadedPresentationName``
     - String
     - Name of the pre-uploaded presentation.
   * - ``allowPromoteGuestToModerator``
     - Boolean
     - Allow moderators to promote guests to moderators.

For more details on the create API call, refer to the `BigBlueButton API documentation <https://docs.bigbluebutton.org/development/api/#get-post-create>`_.
