from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,Text,func,ForeignKey
from sqlalchemy.orm import relationship

class DomainDB(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    domain_name = Column(String(255), nullable=False)
    remarks = Column(Text, nullable=True)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    

    phc_domain_details = relationship("Phc_domain_detailsDB", back_populates="domains")
    
    user = relationship("UsersDB", back_populates="domains")