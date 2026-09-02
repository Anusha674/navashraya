import psycopg2
from app.core.config import settings

def get_db_connection():
    """
    Creates a new connection to the PostGIS PostgreSQL database with quick 2s timeout.
    """
    return psycopg2.connect(
        host=settings.POSTGRES_SERVER,
        port=settings.POSTGRES_PORT,
        database=settings.POSTGRES_DB,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        connect_timeout=2
    )
