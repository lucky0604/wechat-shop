import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative
class Base:
    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    create_time = Column(DateTime, default = datetime.now, server_default = func.now(), comment = "创建时间")
    update_time = Column(DateTime, default = datetime.now, onupdate = datetime.now, server_default = func.now(), server_onupdate = func.now(), comment = "更新时间")
    is_delete = Column(Integer, default = 0, comment = "逻辑删除：0=未删除 1=删除", server_default = "0")

    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        import re
        name_list = re.findall(r"[A-Z][a-z\d]*", cls.__name__)
        return "_".join(name_list).lower()

def gen_uuid() -> str:
    return uuid.uuid4().hex