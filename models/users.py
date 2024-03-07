from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid


class UsersDB(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True, unique=True)
    password = Column(String(255), nullable=False)
    status = Column(Integer, default=0)
    remember_token = Column(String(100), nullable=True, default=None)
    email_verified_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    domains = relationship("DomainDB", back_populates="user")
    
    phc_details = relationship("Phc_detailsDB", back_populates="user")
    
    phc_domain_details = relationship("Phc_domain_detailsDB", back_populates="user")
    
    phc_tbc_code = relationship("Phc_tbc_codeDB", back_populates="user")
    
    phc_tbc_user_details = relationship("Phc_tbc_user_detailsDB", back_populates="user")
    
    roles = relationship("RolesDB", back_populates="user")
    
    specializations = relationship("SpecializationDB", back_populates="user")
    
    task_details = relationship("Task_detailsDB", back_populates="user")
    
    tasks = relationship("TasksDB", back_populates="user")
    
    zones = relationship("ZoneDB", back_populates="user")
    
    
    
    
    
    
    
    
    
    