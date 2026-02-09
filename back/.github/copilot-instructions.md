# Copilot Instructions for Aluguel Backend

## Project Overview
**Aluguel** is a Django REST Framework (DRF) project for managing rental/lease operations (Portuguese: "aluguel" = rental). This is a backend API built on:
- **Framework:** Django 6.0.1 with Django REST Framework 3.16.1
- **Database:** SQLite (development) via `db.sqlite3`
- **Project Structure:** `aluguel/` is the main Django project; `api/` is the primary application

## Architecture & Key Components

### Directory Structure
- **`aluguel/`** - Project-level configuration (settings, URLs, WSGI/ASGI)
  - `settings.py` - Django configuration (database, installed apps, middleware)
  - `urls.py` - Root URL routing (currently only admin at `/admin/`)
  - `wsgi.py` / `asgi.py` - Application servers
  
- **`api/`** - Main Django application for business logic
  - `models.py` - Data models (ORM definitions) - **START HERE for domain understanding**
  - `views.py` - API endpoints and business logic
  - `serializers.py` (when created) - DRF serializers for request/response validation
  - `migrations/` - Database schema versions

### Critical File Relationships
1. **Models** → **Serializers** → **Views** is the DRF data flow
2. Changes to models require: `python manage.py makemigrations` then `python manage.py migrate`
3. URL routing happens in `aluguel/urls.py` (use DRF routers for auto-routing)

## Development Workflow

### Essential Commands (from project root)
```bash
# Activate virtual environment (Windows PowerShell)
.\env\Scripts\Activate.ps1

# Run development server on http://localhost:8000
python manage.py runserver

# Create migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Access Django admin at http://localhost:8000/admin/
# Default superuser setup: python manage.py createsuperuser

# Run tests
python manage.py test api

# Interactive Python shell with Django context
python manage.py shell
```

## Project-Specific Patterns & Conventions

### API Development Pattern
1. **Define models** in `api/models.py` - inherit from `django.db.models.Model`
2. **Create serializers** - use DRF's `ModelSerializer` for automatic CRUD validation
3. **Build viewsets** - inherit from DRF's `ViewSet` or `ModelViewSet` for automatic REST actions
4. **Register routes** - use DRF's `DefaultRouter` in `aluguel/urls.py` for auto-routing

### DRF Configuration
- REST Framework is installed in `INSTALLED_APPS` (settings.py)
- No custom authentication configured yet; use Django defaults or add DRF permission classes
- No pagination/filtering configured; add to `settings.py` under `REST_FRAMEWORK` dict if needed

### Environment & Security Notes
- **DEBUG = True** in settings (development only) - change for production
- **SQLite database** suitable for development; migrate to PostgreSQL/MySQL for production
- **Virtual environment:** Located at `env/` - Python packages isolated here
- Dependencies pinned in `requirements.txt`

## Adding Features - Checklist
When implementing a new API endpoint:
1. [ ] Define model in `api/models.py` with appropriate fields and relationships
2. [ ] Run `python manage.py makemigrations && python manage.py migrate`
3. [ ] Create `ModelSerializer` in `api/serializers.py` (if file doesn't exist, create it)
4. [ ] Create `ViewSet` in `api/views.py` with appropriate actions (list, create, retrieve, etc.)
5. [ ] Register viewset in `aluguel/urls.py` using DRF's `DefaultRouter`
6. [ ] Test endpoint: `python manage.py runserver` and verify in browser/Postman

## Key DRF Resources & Patterns
- **Permission Classes:** `rest_framework.permissions.IsAuthenticated`, `IsAdminUser`, etc.
- **Authentication:** Configure in `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']` (settings.py)
- **Status Codes:** Use `rest_framework.status` for proper HTTP responses
- **Validation:** Implement custom validators in serializer's `validate_*()` methods

## Testing Strategy
- Use Django's built-in test framework: `python manage.py test api`
- Test files: `api/tests.py` (or structure as `api/tests/` directory)
- Use DRF's `APITestCase` for API tests: `from rest_framework.test import APITestCase`

## Common Gotchas
- **Migrations not applied?** Always run migrations after pulling code changes
- **Model changes not reflecting?** Create and apply migrations, restart dev server
- **Admin interface missing models?** Register models in `api/admin.py` using `admin.site.register(ModelName)`
- **Import paths:** Use relative imports within app (`from .models import MyModel`)
