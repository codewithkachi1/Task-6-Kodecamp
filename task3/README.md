# Job Application Tracker API

## Overview

This project is a simple FastAPI application that provides a job application tracker API. It allows users to add and view their job applications. The API uses HTTP Basic authentication to authenticate users and filter job applications based on the logged-in user.

## Features

- Users can add job applications
- Users can view their own job applications
- Authentication using HTTP Basic
- Data stored in JSON files

## Endpoints

- POST /applications/: Add a new job application
- GET /applications/: Get all job applications for the logged-in user

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)

## Installation

1. Install the required packages: pip install fastapi uvicorn
2. Run the API: uvicorn main:app --reload

## Usage

1. Add a new job application: POST /applications/ with job_title, company, date_applied, and status in the request body
2. Get all job applications: GET /applications/ with authentication credentials in the request headers

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
