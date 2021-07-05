from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Data:
    chave_publica: Optional[str] = None
    data_cadastro: Optional[datetime] = None
    data_expiracao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
    ativo: Optional[bool] = None


@dataclass
class Field:
    field: Optional[str] = None
    value: Optional[str] = None
    message: Optional[str] = None


@dataclass
class Error:
    code: Optional[str] = None
    message: Optional[str] = None
    fields: Optional[List[Field]] = None


@dataclass
class ChavesDTO:
    data: Optional[Data] = None
    error: Optional[Error] = None
