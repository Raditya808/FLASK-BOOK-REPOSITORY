# FLASK-BOOK-REPOSITORY

A simple Flask-based web application to manage a collection of books. This repository provides a minimal RESTful API and a web interface to add, view, update, and remove book records. It is intended as an educational project and a practical exercise while learning Flask.

## About
This project was built as a learning exercise following the book "Flask Belajar" and through self-study (otodidak). It is intended for practice and experimentation rather than production use. Expect the code and features to reflect a learning project: simple, clear, and easy to extend.

## Theme (UI)
The web UI theme has been customized as part of the learning process. The project uses a frontend theme (e.g., a Bootswatch theme or custom CSS) to demonstrate how to apply and change styles in a Flask app.

How to change the UI theme:
- If the project uses a Bootswatch CDN in `templates/base.html`, replace the Bootswatch stylesheet link with another theme name. Example:
  ```html
  <!-- Example Bootswatch CDN (replace <theme> with a theme name like 'darkly' or 'cerulean') -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/<theme>/bootstrap.min.css">
  ```
- Alternatively, update or add custom CSS in `static/css/style.css` and ensure `base.html` includes it:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  ```
- After changing styles, refresh the browser or clear cache to see updates.

If you'd like, I can:
- Update the repository templates to switch to a specific Bootswatch theme (name the theme you prefer), or
- Provide a small custom stylesheet example to apply a personalized look.

## Features
- RESTful API for CRUD operations on books
- Simple web UI for interacting with the collection
- Persistence using SQLite by default
- Environment-driven configuration
- Ready for local development and containerized deployment

## Table of Contents
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints (example)](#api-endpoints-example)
- [Database](#database)
- [Testing](#testing)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Requirements
- Python 3.8+
- pip
- (Optional) virtualenv or venv
- (Optional) Docker

## Quick Start (local)
1. Clone the repository
   ```bash
   git clone https://github.com/Raditya808/FLASK-BOOK-REPOSITORY.git
   cd FLASK-BOOK-REPOSITORY
   ```

2. Create and activate a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows (PowerShell)
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables and run
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development     # optional: enables debug mode
   flask run
   ```
   Or:
   ```bash
   python -m flask run
   ```

5. Open your browser at http://127.0.0.1:5000

## Configuration
The app reads configuration from environment variables. Common variables:
- FLASK_APP — main application entry (e.g., `app.py`)
- FLASK_ENV — `development` or `production`
- DATABASE_URL — database connection string (default: `sqlite:///books.db`)
- SECRET_KEY — Flask secret key for sessions

You can create a `.env` file and use python-dotenv or a similar tool to load environment variables in development.

## Usage
- Use the web UI to manage books.
- Or interact with the API using curl, HTTPie, Postman, or similar tools.

Example using curl:
```bash
# List books
curl http://127.0.0.1:5000/api/books

# Add a new book
curl -X POST http://127.0.0.1:5000/api/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Example Book","author":"Author Name","year":2020}'
```

## API Endpoints (example)
Note: adjust endpoints to match the implementation in this repo.
- GET /api/books — list all books
- GET /api/books/<id> — retrieve a single book
- POST /api/books — create a new book
- PUT /api/books/<id> — update a book
- DELETE /api/books/<id> — delete a book

## Database
By default the project uses SQLite for simplicity:
- Database file: `books.db` (or as configured by `DATABASE_URL`)
- Migrations: If using Flask-Migrate, run:
  ```bash
  flask db init
  flask db migrate -m "Initial migration"
  flask db upgrade
  ```

## Testing
If tests are included, run them with pytest:
```bash
pip install -r requirements-dev.txt
pytest
```

## Docker (optional)
Build and run with Docker:
```bash
docker build -t flask-book-repo .
docker run -e FLASK_ENV=production -p 5000:5000 flask-book-repo
```

## Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Make changes and add tests
4. Commit and push
5. Open a pull request describing your change

Please follow repository coding style and add tests for new functionality.

## License
This project is provided under the MIT License. See LICENSE file for details.

## Contact
Maintainer: Raditya808  
Repository: https://github.com/Raditya808/FLASK-BOOK-REPOSITORY
