from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,func,ForeignKey
from sqlalchemy.orm import relationship
class RolesDB(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    roles_name = Column(String(255), nullable=False)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    user = relationship("UsersDB", back_populates="roles")
    