# Secure Shopping Cart API

## Overview

This project is a simple FastAPI application that provides a secure shopping cart API. It allows admins to add products and customers to browse and shop. The API uses HTTP Basic authentication and role-based access control to restrict access to admin-only endpoints.

## Features

- Admins can add products
- Customers can browse products
- Authenticated users can add products to cart
- Role-based access control for admin-only endpoints
- Data stored in JSON files

## Endpoints

- POST /admin/add_product/: Add a new product (admin only)
- GET /products/: Get all products (public)
- POST /cart/add/: Add a product to cart (authenticated users only)

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the API)

## Installation

1. Install the required packages: pip install fastapi uvicorn
2. Run the API: uvicorn main:app --reload

## Usage

1. Add a new product: POST /admin/add_product/ with name and price in the request body (admin only)
2. Get all products: GET /products/ (public)
3. Add a product to cart: POST /cart/add/ with product_name in the request body (authenticated users only)

## API Documentation

The API documentation is available at http://localhost:8000/docs. You can use the documentation to test the API endpoints.
