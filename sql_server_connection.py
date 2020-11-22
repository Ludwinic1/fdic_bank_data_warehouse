from sqlalchemy import create_engine
import os

SERVER = os.environ.get("SQL_SERVER_NAME")
DATABASE = os.environ.get("FDIC_BANK_DATABASE_NAME")
DRIVER = os.environ.get("SQL_SERVER_DRIVER")
DATABASE_CONNECTION = f"mssql://@{SERVER}/{DATABASE}?driver={DRIVER}"
engine = create_engine(DATABASE_CONNECTION)