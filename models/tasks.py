from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,Text,func,ForeignKey
from sqlalchemy.orm import relationship

class TasksDB(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    task_name = Column(String(255), nullable=False)
    evidence_of_compliance = Column(String(255), default=None)
    per_visit=Column(Integer, nullable=False)
    staff_availability = Column(String(255), default=None)
    awareness_trained = Column(String(255), default=None)
    remarks = Column(Text, default=None)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    task_details = relationship("Task_detailsDB", back_populates="tasks")
    
    user = relationship("UsersDB", back_populates="tasks")
    