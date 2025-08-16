# Notes API with Token Authentication

## Overview

This project is a simple FastAPI application that provides a notes management API with JWT token authentication. It allows users to create, read, and manage their notes securely.

## Features

- User authentication using JWT tokens
- Create, read notes
- Token-based authentication for secure access
- Data stored in JSON files

## Endpoints

- POST /login/: Login and obtain a JWT token
- POST /notes/: Create a new note (requires token)
- GET /notes/: Get all notes for the authenticated user (requires token)

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)
- python-jose (for JWT token generation and verification)

## Installation

1. Install the required packages: pip install fastapi uvicorn python-jose
2. Run the API: uvicorn main:app --reload

## Usage

1. Login and obtain a JWT token: POST /login/ with username and password in the request body
2. Create a new note: POST /notes/ with title, content, and date in the request body, and the JWT token in the Authorization header
3. Get all notes: GET /notes/ with the JWT token in the Authorization header

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
