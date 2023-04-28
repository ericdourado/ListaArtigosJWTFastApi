from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    '''
    CONFIGURACOES PARA O APP
    '''
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root:root@localhost:3306/biblioteca?charset=utf8mb4'
    DBBaseModel = declarative_base()
    JWT_SECRET: str = 'j7kUqCye2TUYwX7IsjE4Yx718l0FNbBAwKyuJ32G2es'
    '''
    import secrets
    token: str = secrets.token_urlsafe(32)
    '''
    ALGORITHM: str = 'HS256'
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24


    class Config:
        case_sensitive = True 

settings = Settings()
