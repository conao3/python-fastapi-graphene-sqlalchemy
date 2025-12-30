# FastAPI + Graphene + SQLAlchemy

A lightweight Python application demonstrating how to integrate FastAPI with GraphQL (via Graphene) and SQLAlchemy ORM for building modern APIs backed by PostgreSQL.

## Overview

This project provides a practical example of combining three powerful Python libraries:

- **FastAPI** - High-performance async web framework
- **Graphene** - GraphQL implementation for Python
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapper

The application exposes both REST and GraphQL endpoints, with built-in support for GraphiQL, Playground, and Voyager interfaces for exploring your GraphQL schema.

## Features

- REST API endpoints for direct database queries
- GraphQL endpoint with Relay-style connections
- Multiple GraphQL exploration tools (GraphiQL, Playground, Voyager)
- Environment-based configuration using pydantic
- PostgreSQL database integration

## Requirements

- Python 3.8 or higher
- PostgreSQL database
- Poetry (for dependency management)

## Installation

```bash
# Clone the repository
git clone https://github.com/conao3/python-fastapi-graphene-sqlalchemy.git
cd python-fastapi-graphene-sqlalchemy

# Install dependencies
poetry install
```

## Configuration

Create a `.env` file in the project root with your database credentials:

```env
DB_ADDRESS=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

## Usage

Start the development server:

```bash
poetry run uvicorn fastapi_graphene_sqlalchemy.main:app --reload
```

### Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Health check |
| `GET /department` | List all departments (REST) |
| `GET /graphql` | GraphiQL interface |
| `GET /graphql/playground` | GraphQL Playground |
| `GET /graphql/voyager` | GraphQL Voyager |
| `POST /graphql` | GraphQL query endpoint |

### Example GraphQL Query

```graphql
query {
  departments {
    edges {
      node {
        departmentNo
        departmentName
        location
      }
    }
  }
}
```

## Project Structure

```
src/fastapi_graphene_sqlalchemy/
├── main.py            # FastAPI application and routes
├── config.py          # Environment configuration
├── db.py              # Database connection and session management
├── schema.py          # SQLAlchemy models
└── graphene_schema.py # GraphQL type definitions
```

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.

## Author

Naoya Yamashita ([@conao3](https://github.com/conao3))
