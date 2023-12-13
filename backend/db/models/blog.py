from datetime import date

from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship


class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")
    created_at = Column(DateTime, default=date.today())
    is_active = Column(Boolean, default=False)
