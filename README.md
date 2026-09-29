# Task Management API

[![CI](https://github.com/akalmaliky-spec/task-management-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/akalmaliky-spec/task-management-api/actions/workflows/python-app.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

FastAPI backend with JWT authentication, SQLAlchemy (SQLite for dev, PostgreSQL via Docker), and per-user task CRUD.

## Features

- **FastAPI** framework for high-performance async APIs
- **JWT Authentication** with secure password hashing
- **PostgreSQL** database with SQLAlchemy ORM
- **Docker** and Docker Compose for containerization
- **Pydantic** schemas for request/response validation
- **Comprehensive testing** with pytest
- **CI/CD** with GitHub Actions
- **CORS** configuration for frontend integration

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 14+ (optional; SQLite is the default)
- Docker and Docker Compose (optional)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/akalmaliky-spec/task-management-api.git
cd task-management-api
```

2. Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Start the development server:

```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

### Docker Setup

Run with Docker Compose:

```bash
docker-compose up -d
```

This starts:
- FastAPI application on port 8000
- PostgreSQL database on port 5432

## Project Structure

```
task-management-api/
├── app/
│   ├── routers/
│   │   ├── auth.py          # Register / login
│   │   ├── users.py         # Current-user profile
│   │   └── tasks.py         # Task CRUD
│   ├── config.py            # Settings from environment variables
│   ├── database.py          # Engine, session, get_db dependency
│   ├── deps.py              # get_current_user (JWT bearer)
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── security.py          # bcrypt + JWT helpers
│   └── main.py              # FastAPI application
├── tests/                   # pytest suite
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## API Endpoints

### Authentication

- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login with JSON `{"email", "password"}` and get a bearer token

### Users

- `GET /api/v1/users/me` - Get current user profile
- `PATCH /api/v1/users/me` - Update current user

### Tasks

- `GET /api/v1/tasks/` - List your tasks (`?completed=true|false`, `skip`, `limit`)
- `POST /api/v1/tasks/` - Create new task
- `GET /api/v1/tasks/{id}` - Get task by ID
- `PATCH /api/v1/tasks/{id}` - Update task
- `DELETE /api/v1/tasks/{id}` - Delete task

## Development

### Running Tests

```bash
pytest
```

Or with coverage:

```bash
pytest --cov=app --cov-report=html
```

### Code Quality

Lint code:

```bash
ruff check .
mypy --ignore-missing-imports app
```

Format code:

```bash
ruff format .
```

## Configuration

Environment variables (see `.env.example`):

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./tasks.db
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=development   # "production" refuses to start without SECRET_KEY
CORS_ORIGINS=http://localhost:3000
```

## Deployment

### Docker Production

```bash
docker build -t task-management-api .
docker run -p 8000:8000 --env-file .env task-management-api
```

### Health Check

API includes health check endpoint:

```bash
curl http://localhost:8000/health
```

## Security

- Passwords hashed with bcrypt
- JWT tokens with configurable expiration
- CORS configuration for frontend
- SQL injection protection via SQLAlchemy
- Input validation with Pydantic

## Testing

Comprehensive test suite covering:
- Authentication flows
- CRUD operations
- Input validation
- Error handling
- Per-user task isolation

Run tests:

```bash
pytest -v
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/akalmaliky-spec/task-management-api/issues)
- **Documentation**: [API Docs](http://localhost:8000/docs)

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
