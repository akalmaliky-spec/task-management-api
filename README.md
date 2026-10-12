# Task Management API scaffold

This repository is an incomplete FastAPI project scaffold. It currently contains a package marker, dependency list, Docker configuration, CI configuration and placeholder tests. There is no runnable FastAPI application in `app/`, no database model/migration implementation, and no authentication or task CRUD routes.

## Authentication status

**JWT authentication is not implemented.** `PyJWT` and `passlib[bcrypt]` in the dependency list are dependencies only. This repository does not currently receive passwords, hash credentials, issue/validate access tokens, refresh tokens, or authorize user/task operations. Placeholder tests do not verify authentication.

The earlier README described `/api/v1/auth/register`, `/api/v1/auth/login`, `/api/v1/users/me`, task CRUD, Alembic migrations and `uvicorn app.main:app`; those implementations are absent. These endpoints and commands must not be treated as operational or production-ready.

## Next implementation requirements

Before exposing this scaffold as an API, implement and test:

- An application entry point, models, routes and migrations.
- A generated environment signing key, bcrypt password policy on creation and changes, and immutable user identifiers in expiring access tokens.
- Authentication on private routes, administrator controls and per-task ownership checks.
- Refresh rotation, revocation on logout/password changes, inactive-account denial and login rate limiting.
- HTTPS deployment, secure token storage in clients, explicit CORS configuration and secret-safe logging.

The implemented sibling [Detroit Family Home Care API](https://github.com/akalmaliky-spec/detroit-family-home-care-api) can be used as a reference after its security-hardening changes are reviewed and merged. Do not copy development/default secrets into a deployment.

## Development files

- `app/__init__.py`: package marker only.
- `requirements.txt`: candidate dependencies.
- `Dockerfile`, `docker-compose.yml`: scaffold configurations; their referenced app entry point is not implemented. Database credentials are development examples and must be replaced before any deployment.
- `tests/`: placeholder assertions, not authentication coverage.

This documentation change reports the repository's actual state; it does not create the missing service.
