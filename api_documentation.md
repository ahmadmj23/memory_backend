# Memory Backend API Documentation

This document provides documentation for the authentication, reviews, and artifacts APIs.

## Authentication App
Base URL: `/api/auth/`

### 1. Signup
- **Description:** Register a new user account. Requires email verification via OTP.
- **URL:** `/api/auth/signup`
- **Method:** `POST`
- **Input:**
  - `username` (string, required)
  - `email` (string, required, unique)
  - `password` (string, required, min 8 chars)
- **Expected Output:**
  - `201 Created`: `{"message": "User created successfully. Please verify your email.", "email": "user@example.com"}`

### 2. Login
- **Description:** Authenticate user and obtain access/refresh tokens.
- **URL:** `/api/auth/login`
- **Method:** `POST`
- **Input:**
  - `username` (string, required)
  - `password` (string, required)
- **Expected Output:**
  - `200 OK`: `{"refresh": "...", "access": "..."}`

### 3. Verify OTP
- **Description:** Verify user email using the 6-digit code sent during signup.
- **URL:** `/api/auth/verify-otp`
- **Method:** `POST`
- **Input:**
  - `email` (string, required)
  - `otp` (string, required, 6 digits)
- **Expected Output:**
  - `200 OK`: `{"message": "Account verified successfully. You can now login."}`

### 4. User Detail
- **Description:** Retrieve details of the currently authenticated user.
- **URL:** `/api/auth/user`
- **Method:** `GET`
- **Input:** None (Requires Bearer Token)
- **Expected Output:**
  - `200 OK`: `{"id": 1, "username": "...", "email": "...", "role": "...", "is_verified": true}`

### 5. Logout
- **Description:** Logout the user (placeholder for token blacklisting).
- **URL:** `/api/auth/logout`
- **Method:** `POST`
- **Input:** None (Requires Bearer Token)
- **Expected Output:**
  - `200 OK`: `{"message": "Successfully logged out."}`

### 6. Token Refresh
- **Description:** Renew the access token using a refresh token.
- **URL:** `/api/auth/token/refresh`
- **Method:** `POST`
- **Input:**
  - `refresh` (string, required)
- **Expected Output:**
  - `200 OK`: `{"access": "..."}`

---

## Artifacts App
Base URL: `/api/artifacts/`

### 1. List/Create Artifacts
- **Description:** List all artifacts or upload a new one. (Create requires authentication)
- **URL:** `/api/artifacts/`
- **Method:** `GET` / `POST`
- **Input (POST):**
  - `title` (string, required)
  - `description` (string, required)
  - `era` (string, required, e.g. "1990s")
  - `type` (string, required, choices: "image", "video", "audio", "text")
  - `file` (file, required)
- **Expected Output:**
  - `200 OK` (GET): List of artifact objects.
  - `201 Created` (POST): Created artifact object.

### 2. Retrieve/Update/Delete Artifact
- **Description:** Manage a specific artifact.
- **URL:** `/api/artifacts/{id}/`
- **Method:** `GET` / `PUT` / `PATCH` / `DELETE`
- **Input:** Artifact fields (for update)
- **Expected Output:** Artifact object or success message.

### 3. My Artifacts
- **Description:** List all artifacts owned by the authenticated user.
- **URL:** `/api/artifacts/me/`
- **Method:** `GET`
- **Input:** None (Requires Bearer Token)
- **Expected Output:**
  - `200 OK`: Paginated list of user's artifacts.

### 4. Explore Artifacts
- **Description:** Publicly browse approved artifacts.
- **URL:** `/api/artifacts/explore/`
- **Method:** `GET`
- **Input (Query Params):**
  - `type` (string, optional)
  - `era` (string, optional)
  - `search` (string, optional)
- **Expected Output:**
  - `200 OK`: Paginated list of approved artifacts.

---

## Reviews App
Base URL: `/api/review/`

### 1. Review Queue
- **Description:** List all artifacts pending review. (Requires Reviewer role)
- **URL:** `/api/review/queue`
- **Method:** `GET`
- **Input:** None (Requires Bearer Token)
- **Expected Output:**
  - `200 OK`: List of pending artifacts.

### 2. Approve Artifact
- **Description:** Approve a pending artifact. (Requires Reviewer role)
- **URL:** `/api/review/{artifactId}/approve`
- **Method:** `POST`
- **Input:** None
- **Expected Output:**
  - `200 OK`: `{"status": "approved"}`

### 3. Reject Artifact
- **Description:** Reject a pending artifact. (Requires Reviewer role)
- **URL:** `/api/review/{artifactId}/reject`
- **Method:** `POST`
- **Input:** None
- **Expected Output:**
  - `200 OK`: `{"status": "rejected"}`
