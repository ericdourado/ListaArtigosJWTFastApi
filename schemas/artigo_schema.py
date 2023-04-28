from typing import Optional
from pydantic import BaseModel as SCBaseModel, HttpUrl

class ArtigoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int]

    class Config:
        orm_mode = True