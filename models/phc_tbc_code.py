from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, func,Text,ForeignKey
from sqlalchemy.orm import relationship

class Phc_tbc_codeDB(Base):
    __tablename__ = "phc_tbc_code"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    zone_ID = Column(String(36),ForeignKey("zones.id"),default=None)
    phc_detail_ID = Column(String(36),ForeignKey("phc_details.id"), default=None)
    tbc_code = Column(String(255), nullable=False)
    remarks = Column(Text, nullable=True)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    user = relationship("UsersDB", back_populates="phc_tbc_code")
    
    phc_tbc_user_details = relationship("Phc_tbc_user_detailsDB", back_populates="phc_tbc_code")
    
    zones= relationship("ZoneDB",back_populates="phc_tbc_code")
    
    phc_details= relationship("Phc_detailsDB",back_populates="phc_tbc_code")