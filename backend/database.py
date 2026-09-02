from sqlalchemy import create_engine

DATABASE_URL = "postgresql://navashraya:navashraya@localhost:5432/navashraya"

engine = create_engine(DATABASE_URL)