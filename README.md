# Django URL Shortener (task)

A simple URL shortener built with **Python + Django** featuring:
- User registration, login, logout
- Create short links (auto-generated or custom)
- Redirect short URL → original URL
- Dashboard to manage your links (view + delete)
- Click analytics (click count)
- Optional expiration time for links

---

## Features

### Core Features
- **Authentication**
  - Register, Login, Logout
  - Only logged-in users can create/manage URLs

- **URL Shortening**
  - Enter a long URL → get a short URL
  - Redirect works via: `http://127.0.0.1:8000/<short_key>/`

- **URL Management**
  - Dashboard lists your created short URLs
  - Shows: Original URL, Created date, Click count, Expiration (if any)
  - Delete option (owner-only)

- **Basic Analytics**
  - Each redirect increases the `clicks` count

### Bonus Features
- **Custom short keys**
  - Users can choose the short part (example: `mydeal`, `notes123`)
  - Validation prevents duplicates

- **Expiration time**
  - Users can set an expiry date/time
  - Expired links show an “Expired” page instead of redirecting

---

## Tech Stack
- Python 3.x
- Django
- SQLite (default)

---

## Setup Instructions

### 1) Clone / Download Project
Place the project folder anywhere you want.

### 2) Create and activate virtual environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
