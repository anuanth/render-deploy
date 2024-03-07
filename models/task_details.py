from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,Text,Date,ForeignKey,func
from sqlalchemy.orm import relationship

class Task_detailsDB(Base):
    __tablename__ = 'task_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    task_id = Column(String(36),ForeignKey("tasks.id"),default=None)
    assigned_to = Column(String(255), default=None)
    co_assigned_to = Column(String(255), default=None)
    correction_action_plan = Column(String(255), default=None)
    dependent_days = Column(Integer, nullable=False)  
    working_days = Column(Integer, nullable=False)
    start_date = Column(Date, default=None)
    end_date = Column(Date, default=None)
    status_progression = Column(Text, default=None)
    remarks = Column(Text, default=None)
    score = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    tasks = relationship("TasksDB", back_populates="task_details")
    
    user = relationship("UsersDB", back_populates="task_details")
    
    