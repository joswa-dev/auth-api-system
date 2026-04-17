# Authentication API System (FastAPI + JWT)

Secure user authentication backend implementing registration and login workflows using JWT token-based authorization.

## Features

- User registration and login APIs
- Password hashing using bcrypt
- JWT token authentication
- Token-based route protection
- SQLAlchemy ORM database integration
- Structured schema validation using Pydantic
- Swagger UI API testing support

## Tech Stack

Python
FastAPI
JWT Authentication
SQLAlchemy
SQLite
Pydantic
REST API

## API Endpoints

POST /register
POST /login

Returns JWT access token after successful authentication.

## Use Case

Designed as a backend authentication service similar to production login systems used in:

- web applications
- automation dashboards
- industrial monitoring portals
- internal enterprise tools
