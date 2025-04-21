# SWIFT/BIC Code Management System

A Django REST Framework solution for managing SWIFT/BIC bank codes, developed for the Remitly 2025 Intern Home Exercise.

## Features

- Parses and stores SWIFT/BIC code data from CSV files
- RESTful API endpoints for CRUD operations
- Proper handling of headquarters/branch relationships
- Containerized deployment with Docker
- Comprehensive test coverage

## Technologies

- **Backend**: Django 4.x with Django REST Framework
- **Database**: SQLite3 (included in Django)
- **Testing**: pytest with django-pytest plugin
- **Containerization**: Docker with docker-compose

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yanazPL/swift.git swift
   cd swift
   ```

2. Build and start the containers:
   ```bash
   docker compose build
   docker compose up
   ```

3. Apply database migrations:
   ```bash
   docker compose exec django_app python manage.py makemigrations
   docker compose exec django_app python manage.py migrate
   ```

4. Load initial data (optional):
   ```bash
   docker compose exec django_app python manage.py load_input
   ```

## API Endpoints

All endpoints are available at `http://localhost:8080`

### 1. Retrieve SWIFT Code Details
- **GET** `/v1/swift-codes/{swift-code}`
- Returns details for a single SWIFT code (headquarters or branch)
- Headquarters responses include associated branches

### 2. Get All Codes for a Country
- **GET** `/v1/swift-codes/country/{countryISO2code}`
- Returns all SWIFT codes (both headquarters and branches) for specified country

### 3. Add New SWIFT Code
- **POST** `/v1/swift-codes`
- Request body should include all required fields
- Validates country codes and SWIFT code format

### 4. Delete SWIFT Code
- **DELETE** `/v1/swift-codes/{swift-code}`
- Removes the specified SWIFT code from database

## Database Structure

The database models are defined in [`api/models.py`](./app/api/models.py) and include:

- `Code`: Main model storing all SWIFT code information
- Relationships between headquarters and branches are handled via the swift_code field

## Project Structure

| Path | Description |
|------|-------------|
| [`app/api/models.py`](./app/api/models.py) | Django models for SWIFT codes and countries |
| [`app/api/views.py`](./app/api/views.py) | API view logic |
| [`app/api/serializers.py`](./app/api/serializers.py) | DRF serializers |
| [`app/api/urls.py`](./app/api/urls.py) | API routing |

## Testing

Run the test suite with:
```bash
docker compose exec django_app pytest
```

Test files:
- 📄 [`app/api/tests/test_core.py`](./app/api/tests/test_core.py)

Tests cover:
- API endpoint functionality
- Error handling
- Data validation
- Relationship management between branches and headquarters

## Data Loading

Initial data can be loaded from CSV using the custom management command:
```bash
docker compose exec django_app python manage.py load_input
```

The data loading logic is implemented in [`load_input.py`](./app/api/management/commands/load_input.py) and handles:
- Proper parsing of CSV data
- Identification of headquarters/branches
- Country code normalization
- Data validation

## Development

To access the Django shell:
```bash
docker compose exec django_app python manage.py shell
```
