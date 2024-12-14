# sage_bbb
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Pylint](https://img.shields.io/badge/pylint-9-brightgreen)

## Table of Contents
- [sage\_bbb](#sage_bbb)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
    - [Using pip](#using-pip)
    - [Using Poetry](#using-poetry)
  - [Usage](#usage)
    - [Verifying Installation](#verifying-installation)
    - [Creating a Meeting](#creating-a-meeting)
  - [Package Structure](#package-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction
`sage_bbb` is a Python package designed to simplify interaction with the BigBlueButton (BBB) API. BigBlueButton is an open-source web conferencing system ideal for virtual classrooms, online meetings, and remote collaboration.

## Features
- **Meeting Management**: Create, join, end, and retrieve meeting information.
- **Recording Management**: Access, publish, unpublish, and delete recordings.
- **Configuration Management**: Customize the BigBlueButton environment.
- **URL Validation and Checksum Generation**: Ensure secure API requests.

## Installation

### Using pip

1. **Create a Virtual Environment**:
    ```bash
    python -m venv .venv
    ```

2. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```

3. **Install the Package**:
    ```bash
    pip install python-sage-bbb
    ```

### Using Poetry

1. **Install Poetry**: Follow the official installation instructions at the [Poetry website](https://python-poetry.org/docs/#installation).

2. **Create a New Project (Optional)**:
    ```bash
    poetry new myproject
    cd myproject
    ```

3. **Add the Package as a Dependency**:
    ```bash
    poetry add python-sage-bbb
    ```

4. **Activate the Virtual Environment**:
    ```bash
    poetry shell
    ```

## Usage

### Verifying Installation

To verify the installation, run a simple script to import the package:

```python
from sage_bbb.services.client import BigBlueButtonClient

# Initialize the client
bbb_client = BigBlueButtonClient(
    "https://your-bbb-server.com/bigbluebutton/api/",
    "your-security-salt",
)

# Check connection
connection_status = bbb_client.check_connection()
print(f"Connection Status: {connection_status}")
```

### Creating a Meeting

1. **Import the necessary modules**:
    ```python
    from sage_bbb.services.client import BigBlueButtonClient
    ```

2. **Initialize the client**:
    ```python
    bbb_client = BigBlueButtonClient(
        "http://your-bbb-server.com/bigbluebutton/api/",
        "your-security-salt",
    )
    ```

3. **Check the connection**:
    ```python
    connection_status = bbb_client.check_connection()
    print(f"Connection Status: {connection_status}")
    ```

4. **Create a new meeting**:
    ```python
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
    ```

5. **Join the meeting as a moderator**:
    ```python
    join_url_moderator = bbb_client.meetings.join_meeting(
        meeting_id="random-9887584",
        full_name="Moderator",
        password="mp"
    )
    print(f"Join URL (Moderator): {join_url_moderator}")
    ```

6. **Join the meeting as an attendee**:
    ```python
    join_url_attendee = bbb_client.meetings.join_meeting(
        meeting_id="random-9887584",
        full_name="Attendee",
        password="ap"
    )
    print(f"Join URL (Attendee): {join_url_attendee}")
    ```

## Package Structure

- **helpers**: Contains the `Meeting` dataclass for managing meeting-related data.
- **services**: Includes modules for client, configurations, factory, meetings, and recordings.
- **utils**: Provides utility classes for URL validation and checksum generation.

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enhance your virtual collaboration experiences with `sage_bbb` by integrating BigBlueButton’s powerful features into your own applications and automating routine tasks.
