# FLASK-BOOK-REPOSITORY

This repository is a learning project created while following the book
"BELAJAR OTODIDAK FLASK FRAMEWORK PYTHON UNTUK PENGEMBANGAN APLIKASI WEB".
The goal is to learn Flask by building a small book-management application.
This project focuses mainly on backend concepts in Flask (routing, views,
models, REST APIs). Frontend styling is intentionally minimal and only
included to support functionality.

## What this project is
- A small Flask web application to manage a collection of books (create, read, update, delete).
- Built as a learning exercise to practice concepts from the book and self-study.
- Backend-first: most examples and explanations demonstrate Flask app structure,
  routing, request handling, and simple persistence. CSS/theming is minimal.

## What you'll learn
- Basic Flask application structure (app creation, blueprints or routes)
- Handling requests and responses
- Creating a simple RESTful API for CRUD operations
- SQLite integration and basic persistence
- Running the app locally and simple configuration patterns

## Repository contents
- Flask application source code
- Template files and minimal CSS to support forms and lists
- Example scripts to run the app
- A note on WSGI in `01.wsgi app/README.md`

## Quick start (local)
1. Clone the repository
   ```bash
   git clone https://github.com/Raditya808/FLASK-BOOK-REPOSITORY.git
   cd FLASK-BOOK-REPOSITORY
   ```

2. Create and activate a virtual environment (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows (PowerShell)
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables and run
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run
   ```

5. Open your browser at http://127.0.0.1:5000

## To Run 
Open ur Terminal And use cd to ur python directory 
and Type "py python_file.py"

## Notes about UI / Theme
- This project is backend-first. The HTML and CSS are minimal and intended
  only to support using and testing the application.
- To change the look, edit `templates/base.html` (replace Bootswatch CDN link)
  or `static/css/style.css` (add custom styles).
- Example Bootswatch CDN link to replace in `templates/base.html`:
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@5.3.2/dist/<theme>/bootstrap.min.css">
  ```

## API (example)
- GET /api/books — list all books
- GET /api/books/<id> — retrieve a single book
- POST /api/books — create a new book
- PUT /api/books/<id> — update a book
- DELETE /api/books/<id> — delete a book

## Database
- Default: SQLite (`books.db`)
- If using Flask-Migrate:
  ```bash
  flask db init
  flask db migrate -m "Initial migration"
  flask db upgrade
  ```

## Contributing
Contributions are welcome. If you want to improve structure, add tests,
or enhance the frontend for learning purposes, please open an issue or
send a pull request. This repository is intended for learning — contributions
that improve clarity and teaching value are appreciated.

## License
This project is provided under the MIT License. See LICENSE file for details.

## Contact
Maintainer: Raditya808  
Repository: https://github.com/Raditya808/FLASK-BOOK-REPOSITORY
