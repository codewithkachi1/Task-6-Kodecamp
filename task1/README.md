# Secure Student Portal API

## Overview

This project is a simple FastAPI application that provides a secure student portal API. It allows students to register, log in, and view their grades. The API uses HTTP Basic authentication and stores student data in a JSON file.

## Features

- Register students with username and password
- Log in students using HTTP Basic authentication
- View grades for authenticated students
- Store student data in a JSON file

## Endpoints

- POST /register/: Register a new student
- POST /login/: Log in a student
- GET /grades/: View grades for an authenticated student

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)

## Installation

1. Install the required packages: pip install fastapi uvicorn
2. Run the API: uvicorn main:app --reload

## Usage

1. Register a new student: POST /register/ with username and password in the request body
2. Log in a student: POST /login/ with username and password in the request body
3. View grades: GET /grades/ with authentication credentials in the request headers

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.

