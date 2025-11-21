from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class DatasetProfile(Base):
    __tablename__ = "dataset_profiles"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="CASCADE"))
    column_name = Column(String, nullable=False)
    inferred_type = Column(String, nullable=False)
    missing_count = Column(Integer, nullable=False)
    unique_count = Column(Integer, nullable=False)
