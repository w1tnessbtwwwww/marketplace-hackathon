from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.cfg.config import config

async def get_session() -> Session:
    return Session(bind=create_engine(str(config.connection_string), pool_size=20))