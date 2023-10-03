# API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
    - [Upload Video](#upload-video)
    - [Retrieve Video](#retrieve-video)
3. [Request and Response Formats](#request-and-response-formats)
4. [Error Handling](#error-handling)
5. [Testing](#testing)

## 1. Introduction <a name="introduction"></a>

This API documentation provides information on how to use the Chrome Extension project's backend API. The API allows users to upload and retrieve video files for playback.

## 2. Endpoints <a name="endpoints"></a>

### Upload Video <a name="upload-video"></a>

- **Endpoint:** `/upload`
- **HTTP Method:** `POST`
- **Description:** Uploads a video file to the server for storage.

### Retrieve Video <a name="retrieve-video"></a>

- **Endpoint:** `/play/<video_id>`
- **HTTP Method:** `GET`
- **Description:** Retrieves and serves a video file for playback.

## 3. Request and Response Formats <a name="request-and-response-formats"></a>

### Request Format (Upload Video)

- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Parameters:** 
    - `video` (file): The video file to be uploaded.

### Response Format (Upload Video)

- **Status Code:** `200 OK`
- **Body:** 
    ```json
    {
      "message": "Video uploaded successfully"
    }
    ```

### Response Format (Retrieve Video)

- **Status Code:** `200 OK` (for successful retrieval)
- **Content-Type:** Video file format (e.g., `video/mp4`)
- **Body:** Binary video data

## 4. Error Handling <a name="error-handling"></a>

- If the upload fails due to file format or other issues, the API will respond with an appropriate error message and status code.

## 5. Testing <a name="testing"></a>

- Use tools like Postman to test the API endpoints.
- Verify that you can successfully upload and retrieve videos.

