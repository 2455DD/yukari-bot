from typing import Any
from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, mapped_column,relationship

class Image(Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    file_name:Mapped[str] = mapped_column()
    file_path:Mapped[str] = mapped_column()
    hash:Mapped[str] = mapped_column()
    
class Video(Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    file_name:Mapped[str] = mapped_column()
    file_path:Mapped[str] = mapped_column()
    hash:Mapped[str] = mapped_column() 