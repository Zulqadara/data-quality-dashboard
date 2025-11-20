from sqlalchemy import Column, Integer, String, DateTime, func
from app.models.base import Base
from sqlalchemy.orm import relationship


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    stored_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    columns = relationship("DatasetColumn", back_populates="dataset", cascade="all, delete")
