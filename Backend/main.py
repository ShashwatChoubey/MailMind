from fastapi import FastAPI
from Database.database import engine
from fastapi import HTTPException
from sqlalchemy import text,exc
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI(debug = bool(os.getenv("Debug","false").lower() == "true"))

@app.get("/")
def home():
     return {"health":"ok"}

@app.get("/database_health_check")
async def database_health_check():
   try:
          async with engine.connect() as conn:
               await conn.execute(text("select 1"))
               return {"database":"ok"}
   except exc.SQLAlchemyError as e:
     print(e)
     raise HTTPException(status_code= 500,detail ="Database down")
     
