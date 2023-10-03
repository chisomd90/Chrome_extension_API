# Video Upload and Playback API Documentation

This documentation provides an overview of the Video Upload and Playback API, including its endpoints, usage instructions, and dependencies.

## Overview

The Video Upload and Playback API is a Flask-based web application that allows users to upload video files, store them on the server, retrieve a list of uploaded videos, and play videos using unique video IDs.

## Endpoints

### Home

- **Endpoint:** `/`
- **Method:** GET
- **Description:** Returns a simple greeting message as the home page.

### Upload Video

- **Endpoint:** `/upload`
- **Method:** POST
- **Description:** Allows users to upload video files. Upon successful upload, it returns a JSON response with a unique video ID and a success message.

### List Uploaded Videos

- **Endpoint:** `/videos`
- **Method:** GET
- **Description:** Retrieves a list of successfully uploaded videos in JSON format.

### Play Video

- **Endpoint:** `/play/<video_id>`
- **Method:** GET
- **Description:** Displays a video playback page for the specified `video_id`.
