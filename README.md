# Memory Backend (MVP)

A robust, DB-agnostic, and future-proof backend for the Digital Museum Memory Platform. Built with Django, simple yet powerful.

## 🧱 Tech Stack
- **Framework**: Django 5 + Django REST Framework
- **Auth**: JWT (SimpleJWT) + Email OTP Verification
- **Database**: SQLite (MVP), ready for PostgreSQL
- **Storage**: Local Media (MVP), using Django storage abstraction (ready for S3/GCS)
- **Docs**: Swagger / OpenAPI 3 (drf-spectacular)
- **Container**: Docker + Docker Compose

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- OR Python 3.11+ (for local run)

### Setup (Docker)
1. **Configure Environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your Email Host/User/Pass for OTP to work
   ```
2. **Build and Run**:
   ```bash
   docker-compose up --build
   ```
3. **Access**:
   - API: http://localhost:8000/api/
   - Swagger Docs: http://localhost:8000/swagger/
   - Admin: http://localhost:8000/admin/

### Setup (Local)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure `.env` (as above).
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run server:
   ```bash
   python manage.py runserver
   ```

## 🔐 API Modules

### Authentication (`/api/auth/`)
- **Signup**: Register (Generates OTP, inactive account).
- **Verify**: `POST /verify-otp` to activate account.
- **Login**: Get JWT Access/Refresh tokens.
- **Rate Limit**: 5 requests/min for sensitive endpoints.

### Artifacts (`/api/artifacts/`)
- **CRUD**: Manage memory artifacts (Title, Description, Era, Files).
- **Me**: `GET /me` (My artifacts).
- **Explore**: `GET /explore` (Public approved artifacts).
- **Filters**: Type, Era, Search.

### Reviews (`/api/review/`)
- **Queue**: List pending artifacts (Reviewer only).
- **Actions**: Approve/Reject artifacts.

### AI Service (`/api/ai/`)
- **Generate**: Create backstory from artifact descriptions.

## 🧪 Testing with Swagger
Go to `/swagger/`. You can:
- Authorize using `Bearer <access_token>`.
- Simulate file uploads.
- Test all endpoints interactively.

## 🐳 Docker Production Notes
- The current setup uses `runserver` for dev.
- For production, uncomment the `CMD` in `Dockerfile` to use `gunicorn` (after adding it to requirements).
- Set `DEBUG=False` in `.env`.
