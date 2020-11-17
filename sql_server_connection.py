import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
SERVER = ***** # altered for security
DATABASE = ****** # altered for security
DRIVER = *** # altered for security
DATABASE_CONNECTION = f'mssql://@{SERVER}/{DATABASE}?driver={DRIVER}'
engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()
