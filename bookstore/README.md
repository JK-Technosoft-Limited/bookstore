# Bookstore API

## Overview

This project is a simple Bookstore API built with FastAPI. It allows users to manage books and perform user authentication, including sign-up and login functionalities. The API uses JWT tokens for securing endpoints related to book management.

## Features

- **Book Management**: Users can create, update, delete, and retrieve books.
- **User Authentication**: Includes user sign-up and login functionalities.
- **Secure Endpoints**: Uses JWT tokens to secure book management endpoints.

## Technologies

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Passlib**: Comprehensive password hashing library for Python.
- **JWT**: JSON Web Tokens for securely transmitting information between parties.

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sanjay-dandekar-jktech/git
    ```

2. Navigate to the project directory:

    ```bash
    cd bookstore
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`

### API Endpoints

- Book Management

    - POST /books/: Create a new book.
    - PUT /books/{book_id}: Update a book by ID.
    - DELETE /books/{book_id}: Delete a book by ID.
    - GET /books/{book_id}: Get a book by ID.
    - GET /books/: Get all books.

- User Authentication

    - POST /signup: Sign up a new user.
    - POST /login: Log in and receive an access token.

- Health Check
    - GET /health: Check the health of the API.

### Running using Docker

- Use the following command to bring up the bookstore API container

  ```bash
  docker compose up --build -d bookstore
  ```

### License
    This project is licensed under the MIT License - see the LICENSE file for details
