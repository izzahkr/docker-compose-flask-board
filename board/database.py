import os
import psycopg2
from flask import current_app, g

def get_pg_db_conn():
    """Create a connection to the PostgreSQL database."""
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "psql-db"),  # Menggunakan variabel lingkungan untuk fleksibilitas
        database=os.getenv("POSTGRES_DB", "flask_db"),
        user=os.getenv("POSTGRES_USER", "admin"),
        password=os.getenv("POSTGRES_PASSWORD", "P4ssw0rd"),
        port="5432"
    )

def get_db():
    """Get a database connection from Flask's context."""
    if 'db' not in g:
        g.db = get_pg_db_conn()
    return g.db

def close_db(e=None):
    """Close the database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    """Register database-related functions with the app."""
    app.teardown_appcontext(close_db)
    
    # Optionally initialize the database schema
    # Uncomment the following line if you have a schema.sql to run on startup
    # init_db()  

def init_db():
    """Initialize the database with the schema."""
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.cursor().execute(f.read().decode('utf8'))
    db.commit()
