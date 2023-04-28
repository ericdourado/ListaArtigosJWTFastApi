from typing import Optional, List
from pydantic import BaseModel as SCBaseModel, EmailStr
from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(SCBaseModel):
    id: Optional[int]
    nome: str
    email: str
    admin: bool = False

    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

    class Config:
        orm_mode = True

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos:Optional[List[ArtigoSchema]]

class UsuarioSchemaUpdate(UsuarioSchemaBase):
    nome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    admin: Optional[bool]
