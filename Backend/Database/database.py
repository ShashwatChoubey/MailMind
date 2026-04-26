from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
import os

load_dotenv()
database_string = os.getenv("Database_URL")
engine = create_async_engine(database_string)
async_session = async_sessionmaker(engine)

    