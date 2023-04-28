from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ArtigoModel(settings.DBBaseModel):
    __tablename__ = 'artigos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(255))
    descricao: str = Column(String(255))
    url_fonte: str = Column(String(255))
    usuario_id: int = Column(Integer, ForeignKey('usuarios.id'))
    criador = relationship('UsuarioModel', back_populates='artigos', lazy='joined')