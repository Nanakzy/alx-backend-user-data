0x01-Basic_authenticationi

# Simple Basic Authentication API

## Description
This project provides a simple API with basic user authentication.

## Setup
- Install dependencies: `pip3 install -r requirements.txt`
- Start the server: `API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app`

## Endpoints
- `/api/v1/status`: Check API status.
- `/api/v1/unauthorized`: Simulate unauthorized error (returns 401).

## Error Handling
- 401 Unauthorized: Returns `{"error": "Unauthorized"}`.

