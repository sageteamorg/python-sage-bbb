Package Overview
================

``sage_bbb`` is designed with modularity and ease of use in mind. Here’s a brief overview of the package structure:

- **helpers**: Contains the ``Meeting`` dataclass for managing meeting-related data.
- **services**: Includes various modules (client, configurations, factory, meetings, and recordings) to handle different aspects of BigBlueButton functionality.
- **utils**: Provides utility classes for URL validation and checksum generation.

Why Use ``sage_bbb``?
=====================

- **Simplified API Interaction**: Abstracts the complexity of direct API calls, providing a clean and intuitive interface for common tasks.
- **Modularity**: Each component of the package is designed to handle specific functionality, making the codebase easy to understand and extend.
- **Reliability**: By following best practices in API interaction, the package ensures secure and efficient communication with the BigBlueButton server.

Key Features
============

- **Meeting Management**: Create, join, and end meetings effortlessly. Retrieve information about ongoing and past meetings, and check if a meeting is currently running.
- **Recording Management**: Access, publish, unpublish, and delete meeting recordings. Update recording metadata and upload text tracks for better accessibility.
- **Configuration Management**: Retrieve and set configuration XML for customizing the BigBlueButton environment.
- **URL Validation and Checksum Generation**: Ensure URLs are correctly formatted and secure with SHA-1 checksums for API requests.
