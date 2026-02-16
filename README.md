# Task Management API

[![CI](https://github.com/akalmaliky-spec/task-management-api/actions/workflows/ci.yml/badge.svg)](https://github.com/akalmaliky-spec/task-management-api/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Production-grade FastAPI backend with JWT authentication, PostgreSQL database, Alembic migrations, and Docker support.

## Features

- **FastAPI** framework for high-performance async APIs
- **JWT Authentication** with secure password hashing
- **PostgreSQL** database with SQLAlchemy ORM
- **Alembic** for database migrations
- **Docker** and Docker Compose for containerization
- **Pydantic** schemas for request/response validation
- **Comprehensive testing** with pytest
- **CI/CD** with GitHub Actions
- **Structured logging** for production monitoring
- **CORS** configuration for frontend integration

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
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

5. Run database migrations:

```bash
alembic upgrade head
```

6. Start the development server:

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
- Redis (optional) on port 6379

## Project Structure

```
task-management-api/
├── app/
│   ├── api/                 # API routes
│   │   └── v1/
│   │       ├── auth.py      # Authentication endpoints
│   │       ├── users.py     # User management
│   │       └── tasks.py     # Task CRUD
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── core/                # Core utilities
│   ├── config.py            # Application configuration
│   ├── database.py          # Database setup
│   ├── security.py          # Security utilities
│   └── main.py              # FastAPI application
├── alembic/                 # Database migrations
├── tests/                   # Test suite
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker image definition
└── requirements.txt         # Python dependencies
```

## API Endpoints

### Authentication

- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get access token

### Users

- `GET /api/v1/users/me` - Get current user profile
- `PATCH /api/v1/users/me` - Update current user

### Tasks

- `GET /api/v1/tasks/` - List all tasks
- `POST /api/v1/tasks/` - Create new task
- `GET /api/v1/tasks/{id}` - Get task by ID
- `PATCH /api/v1/tasks/{id}` - Update task
- `DELETE /api/v1/tasks/{id}` - Delete task

## Development

### Running Tests

```bash
make test
```

Or with coverage:

```bash
pytest --cov=app --cov-report=html
```

### Code Quality

Lint code:

```bash
make lint
```

Format code:

```bash
ruff format .
```

### Database Migrations

Create new migration:

```bash
alembic revision --autogenerate -m "description"
```

Apply migrations:

```bash
alembic upgrade head
```

Rollback migration:

```bash
alembic downgrade -1
```

## Configuration

Environment variables (see `.env.example`):

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379/0
ENVIRONMENT=development
DEBUG=True
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
- Database transactions

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
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
