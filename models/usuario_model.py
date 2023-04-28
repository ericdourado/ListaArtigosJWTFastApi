from core.configs import settings
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(255), nullable=True)
    email: int = Column(String(255), nullable=False)
    senha: int = Column(String(255), nullable=False)
    admin: bool = Column(Boolean, default=False)
    artigos = relationship(
        'ArtigoModel',
        cascade='all,delete-orphan',
        back_populates='criador',
        uselist=True,
        lazy='joined'
    ) 