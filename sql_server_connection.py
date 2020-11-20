import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
SERVER = 'DESKTOP-PKB226U' # altered for security
DATABASE = 'bank_data' # altered for security
DRIVER = 'SQL Server Native Client 11.0'  # altered for security
DATABASE_CONNECTION = f'mssql://@{SERVER}/{DATABASE}?driver={DRIVER}'
engine = create_engine(DATABASE_CONNECTION)
#connection = engine.connect()