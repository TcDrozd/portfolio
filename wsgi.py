# wsgi.py
from app import app  # your Flask() instance in app/__init__.py or app.py
if __name__ == "__main__":
    app.run()
