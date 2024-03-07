from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,Text,func,ForeignKey
from sqlalchemy.orm import relationship
class ZoneDB(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    zone_name = Column(String(255), nullable=False)
    remarks = Column(Text, nullable=True)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    
    phc_details = relationship("Phc_detailsDB",back_populates="zones")
    
    phc_tbc_code = relationship("Phc_tbc_codeDB",back_populates="zones")
    
    user = relationship("UsersDB", back_populates="zones")
    
    
    
    